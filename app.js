
/**
 * Module dependencies.
 */

var express = require('express');
var routes = require('./routes');
var user = require('./routes/user');
var http = require('http');
var path = require('path');
var fs = require('fs');
var yaml = require('yaml-front-matter');

var jade = require('jade');
var mongo = require('mongodb');
var monk = require('monk');
var db = monk('mongodb://Michelle:michelle@ds027769.mongolab.com:27769/heroku_app21896193');

var app = express();
var server = http.createServer(app);
var io = require('socket.io').listen(server);

// all environments
app.set('port', process.env.PORT || 3000);
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(express.bodyParser());
app.use(express.favicon());
app.use(express.logger('dev'));
app.use(express.json());
app.use(express.urlencoded());
app.use(express.methodOverride());
app.use(express.cookieParser('your secret here'));
app.use(express.session());
app.use(app.router);
app.use(express.static(path.join(__dirname, 'public')));

// development only
if ('development' == app.get('env')) {
  app.use(express.errorHandler());
}

server.listen(app.get('port'));

app.get('/', routes.index);
app.get('/users', user.list);
app.get('/userlist', routes.userlist(db));
app.get('/challengelist', routes.challengelist(db));
app.get('/editchallengelist', routes.editchallengelist(db));
app.get('/newchallenge', routes.newchallenge);
app.post('/addchallenge', routes.addchallenge(db, fs, yaml));
app.post('/deletechallenge', routes.deletechallenge(db));

// Get challenge with this id
app.get('/challenge/:id', routes.challenge(db));
//app.get('/unitchallenge/:id', routes.unitchallenge(db));
app.get('/userchallenge', routes.userchallenge(db));

io.sockets.on('connection', function (socket) {
	console.log('Server: In connection');
	
	socket.on('results', function(results) {
		console.log('got some results!', results);
		db.get('resultscollection').insert(results, {safe: true}, function(err, records){
			console.log('Record added as ' + records);
		});
	});
});
