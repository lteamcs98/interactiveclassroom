module.exports.extractchallenges = extractchallenges;

function extractchallenges(fs, files, callback){
	var challengeJSONs = [];
	var errorCount = 0;

	if (files.userChallenge.length > 1) {
		files.userChallenge.forEach(function(item) {
			fs.readFile(item.path, function(err, data){
				if (err) throw err;
				try {
					data = JSON.parse(data);
					challengeJSONs.push(data);
				} catch (e) {
					console.log(e);
					errorCount++;
				}
				if(challengeJSONs.length == (files.userChallenge.length - errorCount)) {
					return callback(null, challengeJSONs);
				}
			})
		});
	} else {
			fs.readFile(files.userChallenge.path, function(err, data){
					if (err) throw err;
					try {
						data = JSON.parse(data);
						challengeJSONs.push(data);
					} catch (e){
						console.log(e);
					}
					return callback(null, challengeJSONs);
				})
			}
	return (new Error(), null);
}