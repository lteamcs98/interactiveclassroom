
/**
 * Module dependencies.
 */

var express = require('express');
var routes = require('./routes');
var user = require('./routes/user');
var http = require('http');
var path = require('path');

var jade = require('jade');
var hash = require('./pass').hash;
var mongo = require('mongodb');
var mongoose = require('mongoose');
//var monk = require('monk');
//var db = monk('mongodb://Michelle:michelle@ds027769.mongolab.com:27769/heroku_app21896193');

// Mongoose stuff
mongoose.connect('mongodb://Michelle:michelle@ds027769.mongolab.com:27769/heroku_app21896193');
var UserSchema = new mongoose.Schema({
	username: String,
	password: String,
	salt: String,
	hash: String
});
var User = mongoose.model('users', UserSchema)''

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

// Save messages that tell us whether or not authentication was successful
app.use(function(req, res, next) {
	var err = req.session.error;
	var msg = req.session.success;
	delete req.session.error;
	delete req.session.success;
	res.locals.message = '';
	if (err) res.locals.message = '<p class="msg error>' + err + '</p>';
	if (msg) res.locals.message = '<p class="msg success">' + msg + '</p>';
	next();
});

// Authentication functions
function authenticate(name, pass, fn) {
	if (! module.parent) console.log('Authenticating %s:%s', name, pass);
	
	User.findOne({
		username: name
	},
	function(err, user) {
		if (user) {
			if (err) return fn(new Error('Cannot find user'));
			hash(pass, user.salt, function(err, hash) {
				if (err) return fn(err);
				if (hash == user.hash) return fn(null, user);
				fn(new Error('Invalid password'));
			});
		} else {
			return fn(new Error('Cannot find user'));
		}
	});
}

function requiredAuthentication(req, res, next) {
	if (req.session.user) {
		next();
	} else {
		req.session.error = 'Access denied!';
		res.redirect('/login');
	}
}

function userExist(req, res, next) {
	User.count({
		username: req.body.username
	}, function(err, count) {
		if (count === 0) {
			next();
		} else {
			req.session.error = 'User Exist';
			res.redirect('/signup');
		}
	});
}

// development only
if ('development' == app.get('env')) {
  app.use(express.errorHandler());
}

server.listen(app.get('port'));

app.get('/', function(req, res) {
	if (req.session.user) {
		res.send('Welcome ' + req.session.user.username + '<br />' + '<a href='/logout'>Logout</a>');
	} else {
		res.send('Signup');
	}
});

app.post('/signup', userExist, function(req, res) {
	var password = req.body.password;
	var username = req.body.username;
	
	hash(password, function(err, salt, hash) {
		if (err) throw err;
		var user = new User({
			username: username,
			salt: salt,
			hash: hash,
		}).save(function(err, newUser) {
			if (err) throw err;
			authenticate(newUser.username, password, function(err, user) {
				if (user) {
					req.session.regenerate(function() {
						req.session.user = user;
						req.session.success = 'Authenticated as ' + user.username + 
							' Click to <a href="/logout">logout</a>. ' + 
							' You may now access <a href="/restricted">/restricted</a>.';
						res.redirect('/');
					});
				}
			});
		});
	});
});

app.get('/login', function(req, res) {
	res.render('login');
});

app.post('/login', function(req, res) {
	authenticate(req.body.username, req.body.password, function(err, user) {
		if (user) {
			req.session.regenerate(function() {
				req.session.user = user;
				req.session.success = 'Authenticated as ' + user.username + ' Click to <a href="/logout">logout</a>. ' + 
				' You may now access <a href="/restricted">/restricted</a>.';
				res.redirect('/');
			});
		} else {
			req.session.error = 'Authentication failed, please check your username and password.';
			res.redirect('/login');
		}
	});
});

app.get('/logout', function(req, res) {
	req.session.destroy(function() {
		res.redirect('/');
	});
});

app.get('/profile', requiredAuthentication, function(req, res) {
	res.send('Profile page of ' + req.session.user.username + '<br />' + ' Click to <a href="/logout">logoout</a>');
})

app.get('/users', user.list);
app.get('/userlist', routes.userlist(db));
app.get('/challengelist', routes.challengelist(db));
app.get('/newchallenge', routes.newchallenge);
app.post('/addchallenge', routes.addchallenge(db));

// Get challenge with this id
app.get('/challenge/:id', routes.challenge(db));


io.sockets.on('connection', function (socket) {
	console.log('Server: In connection');
	
	socket.on('results', function(results) {
		console.log('got some results!', results);
		db.get('resultscollection').insert(results, {safe: true}, function(err, records){
			console.log('Record added as ' + records);
		});
	});
});