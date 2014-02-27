var passport = require('passport');
var FacebookStrategy = require('passport-facebook').Strategy;
var Account = require('../models/account.js')

passport.use(new FacebookStrategy({
	clientID: '535674716548501',
	clientSecret: '2f842fa7f61eee7368af09f5bb2d4119',
	callbackURL: 'http://localhost:3000/auth/facebook/callback'
}, function(accessToken, refreshToken, profile, done) {
	process.nextTick(function() { // asynchronous
		Account.findOne({ 'username' : profile.username }, function(err, user) {
			if (err) {	// error connecting to database
				return done(err);
			}
			
			if (user) {	// user is found, log them in
				return done(null, user);
			} else {	// make new user account
				user = new Account({
					name: profile.displayName,
					username: profile.username,
					provider: 'facebook'
					//facebook: profile._json
				});
				user.save(function(err) {
					if (err) console.log(err);
					return done(err, user);
				});
			}
		})
	})
}
));