var passport = require('passport');
var Account = require('../models/account');

module.exports = function(app) {
	app.get('/', function(req, res) {
		res.render('login');
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
		passport.authenticate('google', { successRedirect: '/welcome', failureRedirect: '/login' }));

	app.get('/welcome', function(req, res) {
		if (req.user.admin) {
			res.redirect('/admin/home');
		} else if (req.user.instructor) {
			res.redirect('/instructor/home');
		} else {
			res.redirect('/student/home')
		}
	});

	/* Admin View */

	app.get('/admin/home', function(req, res) {
		if (req.user.admin) {
			res.render('home_admin', {'username': req.user.name});
		} else {
			res.render('unauthorized');
		}
	});

	app.get('/admin/userlist', function(req, res) {
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
						'studentlist': students });
				});
			});
		});
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

	/* Instructor View */

	app.get('/instructor/home', function(req, res) {
		if (req.user.instructor) {
			res.render('home_instructor', {'username': req.user.name});
		} else {
			res.render('unauthorized');
		}
	});

	/* Student View */

	app.get('/student/home', function(req, res) {
		res.render('home_student', {'username': req.user.name});
	});

};
