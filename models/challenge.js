// Challenge model

var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var challengeSchema = new Schema({
	challengeId: Number,
	problem: String,
	functionNames: [],
	functionHeaders: [],
	inputArray: [],
	outputArray: [],
	title: String
});

module.exports = mongoose.model('Challenge', challengeSchema);

/*
// code to add a new challenge
challenge = new Challenge({
	challengeId: 1,
	name: 'Sample Test',
	problem: 'Create a function named testFunction that takes one parameter. Just return that parameter.',
	functionNames: ['testFunction'],
	functionHeaders: ['testFunction(oneParam)'],
	inputArray: [['hello'], ['world']],
	outputArray: ['hello', 'world'],
	title: 'Test'
});

challenge.save();
*/