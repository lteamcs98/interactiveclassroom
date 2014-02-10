var MongoClient = require('mongodb').MongoClient;

/*exports*/
exports.getResultsByChallenge = getResultsByChallenge;
exports.resultsPercentageCorrect = resultsPercentageCorrect;
exports.resultsCalculateMean = resultsCalculateMean;
exports.resultsCalculateMean = resultsCalculateMedian;

//Kind of my "main" function
MongoClient.connect('mongodb://Michelle:michelle@ds027769.mongolab.com:27769/heroku_app21896193', function(err, db) {
	if (err){
		return console.dir(err);
	}

  	getResultsByChallenge(db, 1, resultsCalculateMedian); 
});


//Simply finds the results or mongodb documents for a certain challenge
function getResultsByChallenge(db, challengeId, callback) {
	var collection = db.collection('resultscollection');
	var cursor = collection.find({"challenge_id": challengeId}, {"score": 1,"user_id":1, "failed": 1, "_id":0});//.addOption(DBQuery.Option.noTimeout); <= addOption isn't the right function for Node.js mongodb driver..will look this up later
	
	callback(db, cursor);
};

//Calculates percentage of students who got a 100%. Will update this to allow you to query for percentage of students that failed 
//XYZ tests (or the percentage of students who got 100% if failedIndices == null)
function resultsPercentageCorrect(db, cursor, failedIndices){
	var total = 0;
	var correct = 0;

	cursor.toArray(function(err, items) {
		if (err) throw err;

		for (var i = 0; i < items.length; i++){
			if (items[i].score == 100) {
				correct += 1;
			}
			total += 1;
		}
		console.log(correct/total);
	});
}

/*
function resultsPercentageCorrect2(db, cursor, failedIndices){
	var total = 0;
	var correct = 0;

	cursor.toArray(function(err, items) {
		if (err) throw err;

		for (var i = 0; i < items.length; i++){
			if (failedIndices == "null" && items[i].score == 100) {
				correct += 1;
			}
			else {
				for (var j = 0; j < failedIndices.length; j++) {
						
			}
			total += 1;
		}
		console.log(correct/total);
	});
}*/

//Calculates median score for a certain challenge
function resultsCalculateMedian(db, cursor){
	var scores = new Array();
	var total = 0;
	
	cursor.toArray(function(err, items) {
		for (var i = 0; i < items.length; i++){
			scores[i] = items[i].score;
			total += 1;
		}

		scores.sort( function(a , b) { return a - b; } );
		var half = Math.floor(scores.length/2);

		if (scores.length% 2) {
			console.log(scores[half]);
		}
		else {
			console.log((scores[half - 1] + scores[half])/2.0);
		}
	});	
}


//Calculates mean score for a certain challenge
function resultsCalculateMean(db, cursor){
	var total = 0;
	var numScores = 0;

	cursor.toArray(function(err, items) {
		if (err) throw err;

		for (var i = 0; i < items.length; i++){
			total += items[i].score;
			numScores += 1;
		}

		console.log(total/numScores);
	});
}
