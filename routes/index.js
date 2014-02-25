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
            console.log(doc);
			console.log(doc.outputArray);
            res.render('unitchallenge', { "challengeId" : doc.challengeId, "title": doc.title, "problem" : doc.problem, "inputArray": doc.inputArray, "outputArray": doc.outputArray, "functionNames": doc.functionNames });
        });
        //console.log('found challenge! ' + challenge.problem);
    };
};

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
    res.render('newchallenge', { title: 'Add New Challenge'});
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
		console.log("Content of " + req.files.userChallenge.path + ":");
		var msg = error.uploadErrorCheck(data);
		if (msg == true)
		{
			var JSON = yaml.loadFront(data);
			var promise = db.get('challengecollection').insert(JSON);
			function getHash(err, doc)
			{
					var id_string = new String(doc._id);
					id_string = id_string.concat(doc.title);
					id_string = id_string.concat(doc.problem);
					var code = Math.abs(id_string.hashCode());
					doc.challengeId = code;
					console.log('New Document: ', doc);
					var htmlSnippet = '<iframe src=' + '"interactiveclassroom.herokuapp.com/challenge/' + doc.challengeId.toString() + '"></iframe>';
					console.log('in function html snippet: ', code, htmlSnippet);
					res.render('newchallenge', {"errorMsg": "Challenge successfully added!", "htmlSnippet": htmlSnippet});
			}
			promise.on('complete', getHash);
		}
		else 
		{
			res.render('newchallenge', {"errorMsg": msg} );
		}
	});
	// If it worked, set the header so the address bar doesn't still say /adduser
	//res.location("challengelist");
	// Add forward to success page
	//res.redirect("challengelist");
	}
}