// Account model

var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var accountSchema = new Schema({
	id: Number,
	name: String,
	email: String
});

module.exports = mongoose.model('Account', accountSchema);
