var Challenge = require('../models/challenge');
var Submission = require('../models/submission');

module.exports = function(app) 
{
	app.get('/challenge/:id', function(req, res) 
	{
		Challenge.findOne({ challengeId: Number(req.params.id) }, 'title challengeId problem functionNames inputArray outputArray', function(err, chal) 
		{
			Submission.findOne({ userId: req.user.username, challengeId : Number(req.params.id) }, 'code', function(err, sub) 
			{
				var userCode;
				if (sub === null) userCode = ''; 
				else userCode = sub.code;
				
				res.render('challenge', { 'challengeId': chal.challengeId, 'problem': chal.problem, 
				'functionNames': chal.functionNames, 'inputArray': chal.inputArray, 'outputArray': chal.outputArray, 
				'username': req.user.username, 'oldSub': userCode });
			});
		});
	});
	
	app.get('/challengelist', function(req, res) {
		Challenge.find(function(err, challenges) {
			if (err) return console.error(err);
			res.render('challengelist', { 'challengelist': challenges });
		});
	});
}