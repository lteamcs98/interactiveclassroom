// Dependencies
var express = require('express');
var fs = require('fs');
var http = require('http');
var LocalStrategy = require('passport-local').Strategy;
var mongoose = require('mongoose');
var passport = require('passport');
var path = require('path');

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

// var c1 = new Challenge( {"challengeId": 1,
//     "problem": "Write a function called findMax that returns the maximum in an array of integers.",
//     "functionName": "findMax",
//     "inputs": [
//         [
//             1,
//             2,
//             5,
//             7,
//             0
//         ],
//         [
//             4,
//             7,
//             3,
//             8,
//             2
//         ]
//     ],
//     "outputs": [
//         7,
//         8
//     ]} );
// 	
// c1.save();

// Passport Config
passport.use(new LocalStrategy(Account.authenticate()));
passport.serializeUser(Account.serializeUser());
passport.deserializeUser(Account.deserializeUser());

// MongoDB Config
//var MONGOLAB_URI= 'mongodb://Michelle:michelle@ds027769.mongolab.com:27769/heroku_app21896193'
//var mongo = process.env.MONGOLAB_URI // || 'mongodb://localhost'
mongoose.connect('mongodb://Michelle:michelle@ds027769.mongolab.com:27769/heroku_app21896193');

// Routes
require('./routes/passport')(app);
require('./routes/challenge')(app);

// Run server
//app.listen(app.get('port'), function() {
//	console.log('\nExpress server listening on port ' + app.get('port'));
//});

server.listen(app.get('port'));

io.sockets.on('connection', function (socket) {
	console.log('Server: In connection');
	
	socket.on('results', function(results) {
		console.log('got some results!', results);
		db.get('resultscollection').insert(results, {safe: true}, function(err, records){
			console.log('Record added as ' + records);
		});
	});
});