var passport = require('passport');
var Account = require('../models/account');

module.exports = function(app) {
	app.get('/', function(req, res) {
		res.render('login');
	});

	app.get('/login', function(req, res) {
		res.render('login');
	});

	app.get('/auth/google', passport.authenticate('google'));

	app.get('/auth/google/return',
		passport.authenticate('google', { successRedirect: '/challengelist', failureRedirect: '/login' }));

	app.get('/logout', function(req, res) {
		req.logout();
		res.redirect('/');
	});
};
