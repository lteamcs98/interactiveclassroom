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

// Google API Access codes
var GOOGLE_CLIENT_ID = "255376116060.apps.googleusercontent.com";
var GOOGLE_CLIENT_SECRET = "P8uBAyRsvd0IoHBcMuyRLF75";

// Global Config
var app = express();
var server = http.createServer(app);
var io = require('socket.io').listen(server, { log: false });

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

mongoose.connect('mongodb://Michelle:michelle@ds027769.mongolab.com:27769/heroku_app21896193');
/* When we release the app, uncomment this
if (process.argv[2] == null){
	console.log("Mongodb URI missing.");
	process.exit(1);
}
else{
	mongoose.connect(process.argv[2]);// mongodb://Michelle:michelle@ds027769.mongolab.com:27769/heroku_app21896193
}*/

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
		callbackURL: "http://localhost:3000/auth/google/return", //"http://interactiveclassroom.herokuapp.com/auth/google/return",
		scope: "openid profile email"
	},
	function(accessToken, refreshToken, profile, done) {
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
					email: profile._json["email"],
					admin: false,
					instructor: false
				});

				user.save(function(err) {
					if (err) console.log(err);
					return done(err, user);
				})
			}
		})
	}
));

// Routes
require('./routes/auth')(app);
require('./routes/challenge')(app, fs, yaml);

server.listen(app.get('port'));

io.sockets.on('connection', function (socket) {
	console.log('Server: In connection');

	socket.on('results', function(results) {

		console.log('GOT SOME RESULTS', results);

		Submission.remove({ userId: results.userId, challengeId: results.challengeId }, function(err) {
			if (err) return handleError(err);
		});

		var result = new Submission({ userId: results.userId, challengeId: results.challengeId, code: results.userCode, result: results.userPercent });
		result.save(function(err, result) {
			if (err) return console.error(err);
		})
	});
});
