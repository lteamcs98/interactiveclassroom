// Account model: Defines user accounts + access control with information from
// Google OAuth2.0

var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var accountSchema = new Schema({
	id: Number,
	name: String,
	firstName: String,
	lastName: String,
	email: String,
	admin: Boolean,
	instructor: Boolean
});

module.exports = mongoose.model('Account', accountSchema);
