//check for certain fields: challengeId, problem, functionName, inputs, outputs
//check to make sure challengeId
module.exports.uploadErrorCheck = uploadErrorCheck;

function uploadErrorCheck(data){ //data is raw markdown
	var numFields = 0;
	var lines = data.split("\n");
	var fields = ["challengeId", "problem", "functionName", "inputs", "outputs"];

	for (var i = 0; i < lines.length; i++){ //doc or array of documents
		var field = lines[i].split(" ")[0]; 
		field = field.slice(0, field.length - 1);//omit colon
		for (var j = 0; j < fields.length; j++) {
			if (field == fields[j]) {
				numFields += 1;
			}
		}
	}

	if (numFields == 5) {
		return true;
	}
	else {
		var msg = "Missing one of the following essential fields: challenge Id, problem, functionName, inputs, and outputs.";
		return msg;
	}
}

/*
var testMarkDown = "---\n";
testMarkDown += "challengeId: 3\n";
testMarkDown += "problem: Test problem here.\n";
testMarkDown += "functionName: test \n";
testMarkDown += "inputs:\n";
testMarkDown += "- 2\n";
testMarkDown += "- 1\n";
testMarkDown += "outputs:\n";
testMarkDown += "- 3\n";
testMarkDown += "- 4\n";
testMarkDown += "---";

uploadErrorCheck(testMarkDown);
*/
		
