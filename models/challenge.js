// Challenge model

var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var challengeSchema = new Schema({
	challengeId: Number,
	problem: String,
	functionName: String,
	inputs: [],
	outputs: []
});

module.exports = mongoose.model('Challenge', challengeSchema);