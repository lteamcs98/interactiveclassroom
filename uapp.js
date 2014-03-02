// Dependencies
var express = require('express');
var fs = require('fs');
var http = require('http');
var LocalStrategy = require('passport-local').Strategy;
var mongoose = require('mongoose');
var passport = require('passport');
var path = require('path');
var fs = require('fs');
var yaml = require('yaml-front-matter');

// Global Config
var app = express();
var server = http.createServer(app);
var io = require('socket.io').listen(server);

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
var Account = require('./models/account');
var Submission = require('./models/submission')
var Challenge = require('./models/challenge')

/**
 * Module dependencies.
 */
var express = require('express');
var routes = require('./routes');
var http = require('http');
var path = require('path');
var fs = require('fs');
var yaml = require('yaml-front-matter');

// Passport Config
passport.use(new LocalStrategy(Account.authenticate()));
passport.serializeUser(Account.serializeUser());
passport.deserializeUser(Account.deserializeUser());
// passport.serializeUser(function(user, done) {
// 	done(null, user.id);
// });
// 
// passport.deserializeUser(function(id, done) {
// 	User.findbyId(id, function(err, user) {
// 		done(err, user);
// 	});
// });

// Facebook Authentication
require('./routes/facebook-login.js');

// MongoDB Config
//var MONGOLAB_URI= 'mongodb://Michelle:michelle@ds027769.mongolab.com:27769/heroku_app21896193'
//var mongo = process.env.MONGOLAB_URI // || 'mongodb://localhost'
mongoose.connect('mongodb://Michelle:michelle@ds027769.mongolab.com:27769/heroku_app21896193');

// Routes
require('./routes/passport')(app);
require('./routes/challenge')(app, fs, yaml);

// Run server
//app.listen(app.get('port'), function() {
//	console.log('\nExpress server listening on port ' + app.get('port'));
//});

server.listen(app.get('port'));

// FUNCTIONS THAT NEED TO BE ADDED IN THE APPROPRIATE MODULES
/*
app.get('/', routes.index);
app.get('/userlist', routes.userlist(db));
app.get('/challengelist', routes.challengelist(db));
app.get('/editchallengelist', routes.editchallengelist(db));
app.get('/newchallenge', routes.newchallenge);
app.post('/addchallenge', routes.addchallenge(db, fs, yaml));
app.post('/deletechallenge', routes.deletechallenge(db));
*/

io.sockets.on('connection', function (socket) {
	console.log('Server: In connection');
	
	socket.on('results', function(results) {
		console.log('GOT SOME RESULTS', results);
		Submission.remove({ userId: results.userId, challengeId: results.challengeId }, function(err) {
			if (err) return handleError(err);
		});
		
		var result = new Submission({ userId: results.userId, challengeId: results.challengeId, code: results.userCode });
		result.save(function(err, result) {
			if (err) return console.error(err);
		})
	});
});