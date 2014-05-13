var passport = require('passport');
var Account = require('../models/account');

module.exports = function(app) {
	app.get('/', function(req, res) {
		if (req.user) {
			res.redirect('/home');
		} else {
			res.render('login');
		}
	});

	app.get('/login', function(req, res) {
		res.render('login');
	});

	app.get('/logout', function(req, res) {
		req.logout();
		res.redirect('/login');
	});

	app.get('/auth/google', passport.authenticate('google'));

	app.get('/auth/google/return',
		passport.authenticate('google', { successRedirect: '/home', failureRedirect: '/login' }));

	app.get('/home', function(req, res) {
		if (req.user) {
			res.render('home',
				{ 'username': req.user.name,
				'admin': req.user.admin,
				'instructor': req.user.instructor });
		} else {
			res.redirect('/');
		}
	});

	/* Admin View */

	app.get('/admin/userlist', function(req, res) {
		if(req.user)
		{
			if (req.user.admin) {
				Account.find({ admin: true }, function(err, admins) {
					if (err) return handleError(err);

					Account.find({ admin: false, instructor: true },
						function(err, instructors) {
						if (err) return handleError(err);

						Account.find({ admin: false, instructor: false },
							function(err, students) {
							if (err) return handleError(err);
							res.render('userlist', { 'adminlist': admins,
								'instructorlist': instructors,
								'studentlist': students,
								'admin': req.user.admin,
								'instructor': req.user.instructor });
						});
					});
				});
			} else {
				res.render('unauthorized');
			}
		}
		else
		{
			res.redirect('/');
		}
	});

	app.get('/admin/makeadmin/:userId', function(req, res) {
		Account.update({ id: req.params.userId },
			{ admin: true, instructor: true}, function(err) {
				if (err) return handleError(err);
				res.redirect('/admin/userlist');
		});
	});

	app.get('/admin/makeinstructor/:userId', function(req, res) {
		Account.update({ id: req.params.userId },
			{ admin: false, instructor: true}, function(err) {
				if (err) return handleError(err);
				res.redirect('/admin/userlist');
		});
	});

	app.get('/admin/makestudent/:userId', function(req, res) {
		Account.update({ id: req.params.userId },
			{ admin: false, instructor: false}, function(err) {
				if (err) return handleError(err);
				res.redirect('/admin/userlist');
		});
	});
};
