// Challenge model: Defines properties related to individual challenge

var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var challengeSchema = new Schema({
	challengeId: Number,
	problem: String,
	functionNames: [],
	functionHeaders: [],
	inputArray: [],
	outputArray: [],
	title: String,
	visible: Boolean
});

module.exports = mongoose.model('Challenge', challengeSchema);
