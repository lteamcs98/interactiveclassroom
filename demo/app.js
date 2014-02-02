// sources: http://cwbuecheler.com/web/tutorials/2013/node-express-mongo/

/**
 * Module dependencies.
 */

var express = require('express');
var routes = require('./routes');
var user = require('./routes/user');
var http = require('http');
var path = require('path');

// Mongo Database stuff
var mongo = require('mongodb');
var monk = require('monk');
var db = monk('localhost:27017/demo');

var app = express();

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

app.get('/', routes.index);
app.get('/users', user.list);
app.get('/helloworld', routes.helloworld);
app.get('/userlist', routes.userlist(db));
app.get('/newuser', routes.newuser);
app.get('/room', routes.room);
app.post('/adduser', routes.adduser(db));
app.post('/joinroom', routes.joinroom);

http.createServer(app).listen(app.get('port'), function(){
  console.log('Express server listening on port ' + app.get('port'));
});

/*
// Setup the ready route, join room and broadcast to room.
app.post('/joinroom', function(req) {
    req.io.join(req.data)
    req.io.room(req.data).broadcast('announce', {
        message: 'New client in the ' + req.data + ' room. '
    })
})
*/

// Send the client html.
// Doesn't work :(
app.get('/testuser', function(req, res) {
    res.sendfile(__dirname + '/user.html')
})

app = require('express.io')()
app.http().io()