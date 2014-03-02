var MongoClient = require('mongodb').MongoClient;

/*exports*/
exports.getResultsByChallenge = getResultsByChallenge;
exports.resultsPercentageCorrect = resultsPercentageCorrect;
exports.resultsCalculateMean = resultsCalculateMean;
exports.resultsCalculateMean = resultsCalculateMedian;

//Kind of my "main" function
MongoClient.connect('mongodb://Michelle:michelle@ds027769.mongolab.com:27769/heroku_app21896193', function main(err, db) {
	if (err){
		return console.dir(err);
	}

  	var cursor = getResultsByChallenge(db, 1); 

	var testarray = ['0', '1'];

	resultsPercentageFailedTests(db, cursor, testarray);
	
});


//Simply finds the results or mongodb documents for a certain challenge
function getResultsByChallenge(db, challengeId) {
	var collection = db.collection('resultscollection');
	var cursor = collection.find({"challenge_id": challengeId}, 
			{"score": 1,"user_id":1, "failed": 1, "_id":0});//.addOption(DBQuery.Option.noTimeout); <= addOption isn't the right function for Node.js mongodb driver..will look this up later
	return cursor;
};


function resultsPercentageFailedTests(db, cursor, failedIndices){
	var total = 0;
	var correct = 0;

	cursor.toArray(function(err, items) {
		if (err) throw err;
		
		for (var i = 0; i < items.length; i++){
			console.log(items[i]);
			if (arraysEqual(items[i].failed, failedIndices)){
				correct += 1;
			}
			total += 1;
		}
		console.log(correct/total);
		
	});
}
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

/*Credit to Stack Overflow*/
function arraysEqual(a, b) {
	if (a === b) return true;
	if (a == null || b == null) return false;
	if (a.length != b.length) return false;

	// If you don't care about the order of the elements inside
	// the array, you should sort both arrays here.

	for (var i = 0; i < a.length; ++i) {
		if (a[i] !== b[i]) return false;
	}
	return true;
}
