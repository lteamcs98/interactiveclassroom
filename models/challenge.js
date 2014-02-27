// Challenge model

var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var challengeSchema = new Schema({
	challengeId: Number,
	problem: String,
	functionNames: [],
	inputArray: [],
	outputArray: [],
	title: String
});

module.exports = mongoose.model('Challenge', challengeSchema);