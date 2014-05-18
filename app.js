// -------------- END CONFIGURATION --------------

// Dependencies
var express = require('express');
var fs = require('fs');
var http = require('http');
var mongoose = require('mongoose');
var passport = require('passport');
var GoogleStrategy = require('passport-google-oauth').OAuth2Strategy;
var path = require('path');
var util = require('util');
var yaml = require('yaml-front-matter');

// Global Config
var app = express();
var server = http.createServer(app);
var io = require('socket.io').listen(server, { log: false });

// -------------- START CONFIGURATION --------------
// Google API Access codes
var GOOGLE_CLIENT_ID; //= "255376116060.apps.googleusercontent.com";
var GOOGLE_CLIENT_SECRET; //= "P8uBAyRsvd0IoHBcMuyRLF75";

// URI for MongoDB
var MONGO_URI;// = "mongodb://Michelle:michelle@ds027769.mongolab.com:27769/heroku_app21896193";

// Root URL where website is hosted
var ROOT_URL;// = "http://localhost:3000"
try
{
	data = fs.readFileSync('classroom.config', 'utf8');
}
catch(err) 
{
	console.error('You need to create a "classroom.config" file');
	//console.log(err.stack);
	process.exit(0);
}

lines = data.split( /\r?\n/ );
if(lines.length < 4)
{
	console.error('Must have the following 4 configuration variables defined: 1) GOOGLE_CLIENT_ID 2) GOOGLE_CLIENT_SECRET 3) MONGO_URI 4) ROOT_URL');
	process.exit(0);
}

for(var i = 0; i < lines.length; i++)
{
	values = lines[i].split('=');
	if(i == 0)
		GOOGLE_CLIENT_ID=values[1]
	else if (i == 1)
		GOOGLE_CLIENT_SECRET=values[1]
	else if (i == 2)
		MONGO_URI=values[1]
	else if (i == 3)
		ROOT_URL=values[1]
}

io.set('log level', 0);

app.set('port', process.env.PORT || 3000);
app.set('views', __dirname + '/views');
app.set('view engine', 'jade');
app.set('view options', { layout: false });
app.use(express.bodyParser());
app.use(express.cookieParser('your secret here'));
app.use(express.favicon());
app.use(express.logger());
app.use(express.methodOverride());
app.use(express.session());
app.use(express.static(path.join(__dirname, 'public')));
app.use(passport.initialize());
app.use(passport.session());
app.use(app.router);

// Load Models
var Account = require('./models/account')
var Challenge = require('./models/challenge')
var Submission = require('./models/submission')

mongoose.connect(MONGO_URI);

// Passport Config
passport.serializeUser(function(user, done) {
	done(null, user);
});
passport.deserializeUser(function(obj, done) {
	done(null, obj);
});
passport.use(new GoogleStrategy({
		clientID: GOOGLE_CLIENT_ID,
		clientSecret: GOOGLE_CLIENT_SECRET,
		callbackURL: ROOT_URL.concat("/auth/google/return"),
		scope: "openid profile email"
	},
	function(accessToken, refreshToken, profile, done) {

		Account.count({}, function(err, count) {
			if (err) {
				return done(err);
			}

			console.log(count);

			if (count == 0) {
				user = new Account({
					id: profile.id,
					name: profile.displayName,
					firstName: profile._json["given_name"],
					lastName: profile._json["family_name"],
					email: profile._json["email"],
					admin: true,
					instructor: true
				});

				console.log("New admin created");

				user.save(function(err) {
					if (err) console.log(err);
					return done(err, user);
				});
			} else {

				Account.findOne({ 'id' : profile.id }, function(err, user) {
					if (err) {	// Error connecting to database
						return done(err);
					}

					if (user) { // If user is found, log them in
						return done(null, user);
					} else {
						user = new Account({
							id: profile.id,
							name: profile.displayName,
							firstName: profile._json["given_name"],
							lastName: profile._json["family_name"],
							email: profile._json["email"],
							admin: false,
							instructor: false
						});

						console.log("New student created");

						user.save(function(err) {
							if (err) console.log(err);
							return done(err, user);
						});
					}
				})
			}
		});
	}
));

// Routes
require('./routes/auth')(app);
require('./routes/challenge')(app, fs, yaml, ROOT_URL);

server.listen(app.get('port'));

io.sockets.on('connection', function (socket) {

	socket.on('results', function(results) { // client server interaction for code submission

		// Removes the users previous submission with the same challenge id
		Submission.remove({ userId: results.userId, challengeId: results.challengeId }, function(err) {
			if (err) return handleError(err);
		});

		// Adds the users new submission to the submission table
		var result = new Submission({ userId: results.userId, userName: results.personsName, firstName: results.firstName, lastName: results.lastName, challengeId: results.challengeId, challengeName: results.challengeName, code: results.userCode, result: results.userPercent });
		result.save(function(err, result) {
			if (err) return console.error(err);
		})
	});

	// Assign challenges to users
	socket.on('updateChallengeVisibility', function(data) {

		var conditions = { challengeId: data.challengeId };
		var options = { multi: false };

		Challenge.findOne(conditions, 'visible', function(err, chal) {
			// Toggle visibility to opposite of what it was before
			if (chal.visible)
			{
				Challenge.update(conditions, { visible: false },
					options, function(err, numAffected)
				{
					if (err) return console.error(err);
					console.log('Updated visibility of challenge ' + data.challengeId + ' to false');
				});
			} else
			{
				Challenge.update(conditions, { visible: true }, options, function(err, numAffected)
				{
					if (err) return console.error(err);
					console.log('Updated visibility of challenge ' + data.challengeId + ' to true');
				});
			}
		});
	});

	// Delete challenges
	socket.on('deleteChallenge', function(chal) {
		var conditions = { challengeId: chal.challengeId };

		// Delete all submissions corresponding to this challenge
		Submission.find(conditions).remove(function(err) {
			if (err) return console.error(err);
		});

		Challenge.findOne(conditions).remove(function(err) {
			if (err) return console.error(err);
		});
		console.log('Removed challenge ' + chal.challengeId);
	});

});
