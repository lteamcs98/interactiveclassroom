var error = require('../public/js/errorcheck.js');
var parser = require('../public/js/JSON_parse.js');
var hash = require('../public/js/hash.js');

exports.index = function(req, res){
  res.render('index', { title: 'Express' });
};

exports.userlist = function(db) {
    return function(req, res) {
        var collection = db.get('usercollection');
        collection.find({}, {}, function(e, docs){
            res.render('userlist', {
                "userlist" : docs
            });
        });
    };
};

exports.oldchallenge = function(db) {
    return function(req, res) {
        var challenges = db.get('challengecollection');
        challenges.findOne({ challengeId: Number(req.params.id) }, {}, function(e, doc){
            console.log(doc.problem);
            console.log(doc.inputs);
            console.log(doc.outputs);
			console.log(new Array(doc.inputs));
             res.render('challenge', { "challengeId" : doc.challengeId, "problem" : doc.problem, "inputs": doc.inputs, "outputs": doc.outputs, "functionName": doc.functionName});
        });
        //console.log('found challenge! ' + challenge.problem);
    };
};

exports.challenge = function(db) {
    return function(req, res) {

        var challenges = db.get('challengecollection');

        challenges.findOne({ challengeId: Number(req.params.id) }, {}, function(e, doc){

            var userInput = db.get('userResponse');
            userInput.findOne({ user_id: 'd34164d', challenge_id: Number(req.params.id) }, {}, function(e, doc2){

                console.log("\n\n\n");
                console.log(doc);
                console.log(doc.outputArray);
                console.log("\n\n\n");
                console.log(doc2);
                console.log("\n\n\n");

                ///*
                var userInputCode;
                if (doc2 === null) userInputCode =  '';
                else userInputCode = doc2.userCode;
                //*/
                console.log(userInputCode);

                res.render('unitchallenge', 
                    {
                        "challengeId" : doc.challengeId,
                        "title": doc.title,
                        "problem" : doc.problem,
                        "inputArray": doc.inputArray,
                        "outputArray": doc.outputArray,
                        "functionNames": doc.functionNames,
                        "oldSub": userInputCode
                    });
            });
        });
    };
};

/*

exports.challenge = function(db) {
    return function(req, res) {
        var challenges = db.get('challengecollection');
        challenges.findOne({ challengeId: Number(req.params.id) }, {}, function(e, doc){
            console.log(doc);
            console.log(doc.outputArray);
            res.render('unitchallenge', { "challengeId" : doc.challengeId, "title": doc.title, "problem" : doc.problem, "inputArray": doc.inputArray, "outputArray": doc.outputArray, "functionNames": doc.functionNames });
        });
        //console.log('found challenge! ' + challenge.problem);
    };
};

*/
exports.userchallenge = function(db) {
    return function(req, res) {
        var challenges = db.get('challengecollection');
        challenges.findOne({ challengeId: Number(req.params.id) }, {}, function(e, doc){
            console.log(doc);
            res.render('unitchallenge', { "challengeId" : doc.challengeId, "title": doc.title, "problem" : doc.problem, "inputArray": doc.inputArray, "outputArray": doc.outputArray, "functionNames": doc.functionNames });
        });
        //console.log('found challenge! ' + challenge.problem);
    };
};

exports.challengelist = function(db) {
    return function(req, res) {
        var collection = db.get('challengecollection');
        collection.find({}, {'sort': 'challengeId'}, function(e, docs){
            res.render('challengelist', {
                "challengelist" : docs
            });
        });
    };
};

exports.editchallengelist = function(db) {
    return function(req, res) {
        var collection = db.get('challengecollection');
        collection.find({}, {'sort': 'challengeId'}, function(e, docs){
            res.render('editchallengelist', {
                "challengelist" : docs
            });
        });
    };
};

exports.newchallenge = function(req, res){
    res.render('newchallenge', { title: 'Add New Challenge', "iframes": new Array()});
}

exports.deletechallenge = function(db) {
    return function(req, res) {
        var collection = db.get('challengecollection');
        var challengeId = parseInt(req.body.challengeId);
        var selector = { "challengeId" :  challengeId };

        collection.remove(selector);

        // Redirect back to edit challenge list        
        res.location("editchallengelist");
        res.redirect("editchallengelist");
    }
}

exports.addchallenge = function(db, fs, yaml) {
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
					var promise = db.get('challengecollection').insert(JSON);
					function updateID(err, doc)
					{
							var id_string = new String(doc._id);
							id_string = id_string.concat(doc.title);
							id_string = id_string.concat(doc.problem);
							var code = Math.abs(id_string.hashCode());
							doc.challengeId = code;
							docs_id.push(code);
							console.log(docs_id);
							var update_promise = db.get('challengecollection').update( { _id: doc._id }, { title: doc.title, challengeId : code, problem: doc.problem, functionNames: doc.functionNames, inputArray: doc.inputArray, outputArray: doc.outputArray });
							update_promise.on('complete', renderTemplate);
							//console.log('New Document: ', doc);
					}
					function renderTemplate(err, doc)
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
					promise.on('complete', updateID);
				}
				else 
				{
					res.render('newchallenge', {"errorMsg": msg, "iframes": new Array() } );
				}
			}
		});
	}
}
/*

*/
