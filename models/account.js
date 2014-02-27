// Account model

var mongoose = require('mongoose');
var Schema = mongoose.Schema;
var passportLocalMongoose = require('passport-local-mongoose');

var accountSchema = new Schema({
	name: { type: String, default: '' },
	email: { type: String, default: '' },
	username: { type: String, default: '' },
	provider: { type: String, default: '' },
	authToken: { type: String, default: '' },
	//facebook: {}
});

accountSchema.plugin(passportLocalMongoose);

module.exports = mongoose.model('Account', accountSchema);