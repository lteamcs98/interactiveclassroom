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

exports.challenge = function(db) {
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

exports.challengelist = function(db) {
    return function(req, res) {
        var collection = db.get('challengecollection');
        collection.find({}, {}, function(e, docs){
            res.render('challengelist', {
                "challengelist" : docs
            });
        });
    };
};

exports.newchallenge = function(req, res){
    res.render('newchallenge', { title: 'Add New Challenge'});
}

exports.addchallenge = function(db) {
    return function(req, res) {

        // Get our form values
        var challengeId = req.body.challengeId;
        var problem = req.body.problem;
        var functionName = req.body.functionName;
        var inputs = req.body.inputs;
        var outputs = req.body.outputs;

        // Set our collection
        var collection = db.get('challengecollection');

        // Submit to the DB
        collection.insert({
            "challengeId" : challengeId,
            "problem" : problem,
            "functionName" : functionName,
            "inputs" : inputs,
            "outputs" : outputs
        }, function(err,doc) {
            if (err) {
                // If it failed, return error
                res.send("There was a problem adding the information to the database.");
            }
            else {
                // If it worked, set the header so the address bar doesn't still say /adduser
                res.location("userlist");
                // Add forward to success page
                res.redirect("userlist");
            }
        });
    }
}
