// Dependencies
var express = require('express');
var fs = require('fs');
var http = require('http');
var mongoose = require('mongoose');
var path = require('path');
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
app.use(app.router);

// Load Models
var Challenge = require('./models/challenge')

if (process.argv[2] == null){
	console.log("Mongodb URI missing.");
	process.exit(1);
}
else{
	mongoose.connect(process.argv[2]);// mongodb://Michelle:michelle@ds027769.mongolab.com:27769/heroku_app21896193
}

// Routes
require('./routes/challenge')(app, fs, yaml);

server.listen(app.get('port'));

io.sockets.on('connection', function (socket) {
	console.log('Server: In connection');
});
