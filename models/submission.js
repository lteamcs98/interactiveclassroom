// Submission model: Relation between account and challenge

var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var submissionSchema = new Schema({
	challengeId: Number,
	challengeName: String,
	userId: Number,
	userName: String,
	code: String,
	result: Number
});

module.exports = mongoose.model('Submission', submissionSchema);
