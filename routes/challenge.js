var Challenge = require('../models/challenge');
var Submission = require('../models/submission');
var error = require('../public/js/errorcheck.js');
var hash = require('../public/js/hash.js');
var visitors = 0

module.exports = function(app, fs, yaml)
{
	app.get('/', function(req, res) {
		Challenge.find(function(err, challenges) {
			if (err) return console.error(err);
			res.render('challengelist', { 'challengelist': challenges });
		});
	});

	app.get('/results/:id', function(req, res)
	{
		 Submission.find({ challengeId : Number(req.params.id) }, 'result', function(err, submissions)
		 {

		 	var attempted = 0;
			var percentage = 0;

			submissions.forEach(function(submiss){

				attempted = attempted + 1;
				percentage = percentage + submiss.result;
				//console.log(submiss);

			});

			//console.log('\n\n', percentage);
			percentage = percentage / attempted;
			//console.log('\n\n', percentage);

			res.render('results',{
				'attempted': attempted,
				'percentage': percentage,
			});

		 });
	});

	app.get('/challenge/:id', function(req, res)
	{
        visitors += 1;
        console.log('visitor: ', visitors);
		if (! req.user) {
			res.redirect('/');
		} else {

			Challenge.findOne({ challengeId: Number(req.params.id) }, 'title challengeId problem functionNames functionHeaders inputArray outputArray', function(err, chal)
			{
				Submission.findOne({ userId: Number(req.user.id), challengeId : Number(req.params.id) }, 'challengeId userId code', function(err, sub)
				{
					var userCode;
					if (sub === null) userCode = setEditorValue(chal.functionHeaders);
					else userCode = sub.code;

					res.render('challenge', {
						'personsID': Number(req.user.id),
						'oldSub': userCode,
						'challengeId': chal.challengeId,
						'problem': chal.problem,
						'functionNames': chal.functionNames,
						'functionHeaders': chal.functionHeaders,
						'inputArray': chal.inputArray,
						'outputArray': chal.outputArray
					});
				});
			});
		}
	});

	function setEditorValue(headers)
	{
		var editorString = '';
		for(var i = 0; i < headers.length; i++)
		{
			editorString += 'function ' + headers[i] + '\n{\n\n}\n\n';
		}
		return editorString;
	}

	app.get('/challengelist', function(req, res) {
		console.log(req.user);
		console.log(req.user.id);
		Challenge.find(function(err, challenges) {
			if (err) return console.error(err);
			res.render('challengelist', { 'challengelist': challenges });
		});
	});

	app.get('/editchallengelist', function(req, res) {
		Challenge.find(function(err, challenges) {
			if (err) return console.error(err);
			res.render('editchallengelist', { 'challengelist': challenges });
		});
	});


	app.post('/deletechallenge', function(req, res) {
		var challengeId = parseInt(req.body.challengeId);
		var selector = { "challengeId" :  challengeId };

		Challenge.findOne(selector).remove(function(err) {
			if (err) return console.error(err);
		});

        // Redirect back to edit challenge list
        res.location("editchallengelist");
        res.redirect("editchallengelist");
	});

	app.get('/newchallenge', function(req, res){
		res.render('newchallenge', { title: 'Add New Challenge', "iframes": new Array()});
	});

	app.post('/addchallenge', addChallenge(fs, yaml));

	function addChallenge(fs, yaml) {
		return function(req, res) {
			// Print to console the contents of user uploaded challenge.
			fs.readFile(req.files.userChallenge.path, 'utf8', function(err, data) {
				if (err) throw err;
				var mdDocs = parser.parseMarkdown(data);
				console.log(mdDocs);
				var docs_id = new Array();
				var htmlSnippets = new Array();
				for (var i = 0; i < mdDocs.length; i++)
				{
					//console.log(mdDocs[i]);
					var msg = error.uploadErrorCheck(mdDocs[i]);
					if (msg == true)
					{
						var JSON = yaml.loadFront(mdDocs[i]);
						//var promise = db.get('challengecollection').insert(JSON);
						var newChallenge = new Challenge({"challengeId" : JSON.challengeId, "problem" : JSON.problem, "functionNames" : JSON.functionNames, "inputArray" : JSON.inputArray, "outputArray" : JSON.outputArray, "title" : JSON.title });
						newChallenge.save();
						console.log('NEW CHALLENGE CREATED!', newChallenge);
						updateID(newChallenge);
						console.log('NEW CHALLENGE UPDATED!', newChallenge);
						renderTemplate();

						function updateID(doc)
						{
								var id_string = new String(doc._id);
								id_string = id_string.concat(doc.title);
								id_string = id_string.concat(doc.problem);
								var code = Math.abs(id_string.hashCode());
								doc.challengeId = code;
								docs_id.push(code);
								console.log(docs_id);
								doc.update({ '_id': doc._id }, { 'title': doc.title, 'challengeId' : code, 'problem' : doc.problem, 'functionNames' : doc.functionNames, 'inputArray' : doc.inputArray, 'outputArray' : doc.outputArray });
								console.log(doc);
								//var update_promise = db.get('challengecollection').update( { _id: doc._id }, { title: doc.title, challengeId : code, problem: doc.problem, functionNames: doc.functionNames, inputArray: doc.inputArray, outputArray: doc.outputArray });
								//update_promise.on('complete', renderTemplate);
								//console.log('New Document: ', doc);
						}
						function renderTemplate()
						{
							console.log('Challenge IDs: ', docs_id);
							var htmlSnippet = '<iframe src=' + '"http://interactiveclassroom.herokuapp.com/challenge/' + docs_id[htmlSnippets.length] + '"></iframe>';
							htmlSnippets.push(htmlSnippet);
							console.log('hello world!', htmlSnippets.length , mdDocs.length);
							if(htmlSnippets.length == mdDocs.length)
							{
								console.log('snippets: ', htmlSnippets);
								res.render('newchallenge', {"errorMsg": "Challenge successfully added!!!", "iframes": htmlSnippets});
							}
						}
						//promise.on('complete', updateID);
					}
					else
					{
						res.render('newchallenge', {"errorMsg": msg, "iframes": new Array() } );
					}
				}
			});
		}
	}
}
