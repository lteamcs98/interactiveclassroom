
/**
 * Module dependencies.
 */

var express = require('express');
var routes = require('./routes');
var user = require('./routes/user');
var http = require('http');
var path = require('path');

var mongo = require('mongodb');
var monk = require('monk');
var db = monk('localhost:27017/demo');

var app = express();
var server = http.createServer(app);
var io = require('socket.io').listen(server, {log : false});

// all environments
app.set('port', process.env.PORT || 3000);
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');
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

app.get('/client', routes.client);
app.get('/', routes.index);
app.get('/users', user.list);
app.get('/helloworld', routes.helloworld);
app.get('/userlist', routes.userlist(db));

io.sockets.on('connection', function (socket) {
	console.log('Server: In connection');

	socket.on('requestChallenge', function() {
		console.log('Server: In request challenge');
		socket.emit('sendChallenge',
			{
				problem: 'Write a function called findMax() that returns the maximum in an array of integers.',
				functionName: 'findMax',
				input: [ [1, 2, 5, 7, 0], [4, 7, 3, 8, 2]],
				output: [7, 8]
			});
    // send data to client: prompt, input, and output
	});

});

io.sockets.on('requestChallenge', function(socket) {
	console.log('Server: In request challenge');
	socket.emit('sendChallenge', { problem: 'write a for loopsdfsdafsdafsdfdssdsfdsf' });
    // send data to client: prompt, input, and output
});