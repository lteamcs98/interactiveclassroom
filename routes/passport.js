var passport = require('passport');
var Account = require('../models/account');

module.exports = function(app) {
	app.get('/', function(req, res) {
		res.render('index', { user : req.user });
	});

	app.get('/register', function(req, res) {
		res.render('register', {});
	});

	app.post('/register', function(req, res) {
		Account.register(new Account({ username : req.body.username }), req.body.password, function(err, account) {
			if(err) {
				return res.render('register', { account : account });
			}

			passport.authenticate('local')(req, res, function() {
				res.redirect('/');
			});
		});
	});

	app.get('/login', function(req, res) {
		res.render('login', { user : req.user });
	});

	app.post('/login', passport.authenticate('local'), function(req, res) {
		res.redirect('/');
	});

	app.get('/auth/google', passport.authenticate('google'));

	app.get('/auth/google/return',
		passport.authenticate('google', { successRedirect: '/challengelist', failureRedirect: '/login' }));

	app.get('/logout', function(req, res) {
		req.logout();
		res.redirect('/');
	});
};
