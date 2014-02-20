// Submission model

var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var submissionSchema = new Schema({
	challengeId: Number,
	userId: Number,
	problem: String,
	functionName: String,
	inputs: [],
	outputs: []
});

module.exports = mongoose.model('Submission', submissionSchema);