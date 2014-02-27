// Submission model

var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var submissionSchema = new Schema({
	challengeId: Number,
	userId: String,
	code: String
});

module.exports = mongoose.model('Submission', submissionSchema);