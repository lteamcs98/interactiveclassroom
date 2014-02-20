var Challenge = require('../models/challenge');
var Submission = require('../models/submission');

module.exports = function(app) {
	app.get('/challenge/:id', function(req, res) {
		Challenge.findOne({ challengeId: Number(req.params.id) }, 'title challengeId problem functionName inputs outputs', 
		function(err, chal) {
			res.render('challenge', { 'challengeId': chal.challengeId, 'problem': chal.problem, 
			'functionName': chal.functionName, 'inputs': chal.inputs, 'outputs': chal.outputs, 
			'username': req.user.username });
		});
	});
}