// Submission model: Relation between account and challenge

var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var submissionSchema = new Schema({
	challengeId: Number,
	userId: Number,
	code: String,
	result: Number
});

module.exports = mongoose.model('Submission', submissionSchema);
