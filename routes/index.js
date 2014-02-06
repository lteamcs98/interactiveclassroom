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