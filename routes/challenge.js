var Challenge = require('../models/challenge');
var Submission = require('../models/submission');
var error = require('../public/js/errorcheck.js');
var challengeJSONs = require('../public/js/extractchallenges.js');
var hash = require('../public/js/hash.js');

module.exports = function(app, fs, yaml)
{
	app.get('/', function(req, res) {
		Challenge.find(function(err, challenges) {
			if (err) return console.error(err);
			res.render('challengelist', { 'challengelist': challenges });
		});
	});

	app.get('/results', function(req, res)
	{
		 Submission.find({}, 'challengeId result', function(err, submissions)
		 {

		 	var numberOfChallenges = 0;

			submissions.forEach(function(submiss){
			
				if (submiss.challengeId > numberOfChallenges){
					numberOfChallenges = submiss.challengeId;
				}

			});

			//console.log("Highest challenge number: " + numberOfChallenges);

			var attemptedList = new Array(numberOfChallenges + 1);
			var percentageList = new Array(numberOfChallenges + 1);

			for (apple = 0; apple <= numberOfChallenges; apple++){
				attemptedList[apple] = 0;
				percentageList[apple] = 0;
			}

			submissions.forEach(function(submiss){
				
				//console.log(submiss.challengeId + " --- " + submiss.result);
				attemptedList[submiss.challengeId] += 1;
				percentageList[submiss.challengeId] += submiss.result;

			});

			//console.log(attemptedList);
			//console.log(percentageList);

			for (inc = 0; inc <= numberOfChallenges; inc++){

				if (attemptedList[inc] != 0){
					
					percentageList[inc] = percentageList[inc] / attemptedList[inc];
				}
			}

			//console.log('\n\n', percentage);

			res.render('allResults',{
				'numberOfChallenges': numberOfChallenges,
				'attemptedList': attemptedList,
				'percentageList': percentageList
			});

		 });
	});

	app.get('/results/:id', function(req, res)
	{
		//console.log("Am I getting here?");

		 Submission.find({ challengeId : Number(req.params.id) }, 'userName result', function(err, submissions)
		 {
		 	
		 	var userNameList = new Array();
			var resultList = new Array();

			var index = 0;

			submissions.forEach(function(submiss){
				
				console.log(index);
				console.log(submiss.userName);
				
				userNameList[index] = submiss.userName;
				resultList[index] = submiss.result;

				index = index + 1;

			});

			res.render('challengeResults',{
				'userNameList': userNameList,
				'resultList': resultList
			});

		 });
	});

	app.get('/myResults', function(req, res)
	{
		//console.log("Am I getting here?");

		 Submission.find({ userId: Number(req.user.id) }, 'challengeId userName result', function(err, submissions)
		 {
		 	
			var resultList = new Array();

			submissions.forEach(function(submiss){
				
				console.log(submiss.challengeId);
				console.log(submiss.result);

				resultList[submiss.challengeId] = submiss.result;

			});

			res.render('myResults',{
				'resultList': resultList,
			});

		 });
	});

	app.get('/challenge/:id', function(req, res)
	{
		if (! req.user) {
			res.redirect('/');
		}
		else {

			Challenge.findOne({ challengeId: Number(req.params.id) }, 'title challengeId problem functionNames functionHeaders inputArray outputArray', function(err, chal)
			{
				Submission.findOne({ userId: Number(req.user.id), challengeId : Number(req.params.id) }, 'challengeId userId code', function(err, sub)
				{
					var userCode;
					if (sub === null) userCode = setEditorValue(chal.functionHeaders);
					else userCode = sub.code;

					console.log("\n\nThis is from challenge.js: "
						+ String(req.user.name)
						+ "\n\n");

					res.render('challenge', {
						'personsID': Number(req.user.id),
						'theirName': req.user.name,
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

		// example code for extracting challenges
		// challengeJSONs.extractchallenges(fs, req.files, addChallenges);
		// function addChallenges(err, data) {
		// 	console.log("challengeJSONs");
		// 	console.log(data);
		// }

		return function(req, res) {
			// Print to console the contents of user uploaded challenge.
			fs.readFile(req.files.userChallenge.path, 'utf8', function(err, data) {
				if (err) throw err;
				eval("var data = " + data);
				var docs_id = new Array();
				var htmlSnippets = new Array();
				var msg = error.uploadErrorCheck(data);

				if (msg == true)
				{
					//var promise = db.get('challengecollection').insert(JSON);
					var newChallenge = new Challenge({"challengeId" : data.challengeId, "problem" : data.problem, "functionNames" : data.functionNames, "inputArray" : data.inputArray, "outputArray" : data.outputArray, "title" : data.title, "functionHeaders": data.functionHeaders });
					newChallenge.save();
					//console.log('NEW CHALLENGE CREATED!', newChallenge);
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
							//console.log(docs_id);
							doc.update({ '_id': doc._id }, { 'title': doc.title, 'challengeId' : code, 'problem' : doc.problem, 'functionNames' : doc.functionNames, 'inputArray' : doc.inputArray, 'outputArray' : doc.outputArray, 'functionHeaders' : doc.functionHeaders });
							//console.log(doc);
							//var update_promise = db.get('challengecollection').update( { _id: doc._id }, { title: doc.title, challengeId : code, problem: doc.problem, functionNames: doc.functionNames, inputArray: doc.inputArray, outputArray: doc.outputArray });
							//update_promise.on('complete', renderTemplate);
							//console.log('New Document: ', doc);
					}
					function renderTemplate()
					{
						console.log('Challenge IDs: ', docs_id);
						var htmlSnippet = '<iframe src=' + '"http://interactiveclassroom.herokuapp.com/challenge/' + docs_id[htmlSnippets.length] + '"></iframe>';
						htmlSnippets.push(htmlSnippet);
						console.log('hello world!', htmlSnippets.length , data.length);
						//if(htmlSnippets.length == data.length) *** Commented out until data is an array
						//{
							console.log('snippets: ', htmlSnippets);
							res.render('newchallenge', {"errorMsg": "Challenge successfully added!!!", "iframes": htmlSnippets});
						//}
					}
					//promise.on('complete', updateID);
				}
				else
				{
					res.render('newchallenge', {"errorMsg": msg, "iframes": new Array() } );
				}
				
			});
		}
	}
}
