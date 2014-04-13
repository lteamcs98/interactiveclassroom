// Account model

var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var accountSchema = new Schema({
	id: Number,
	name: String,
	email: String,
	admin: Boolean,
	instructor: Boolean
});

module.exports = mongoose.model('Account', accountSchema);
