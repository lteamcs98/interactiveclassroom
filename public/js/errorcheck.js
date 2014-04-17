//check for certain fields: challengeId, problem, functionName, inputs, outputs
//check to make sure challengeId
module.exports.uploadErrorCheck = uploadErrorCheck;

function uploadErrorCheck(data){ //data is one JSON object
	var fields = ["title", "challengeId", "problem", "functionHeaders", "functionNames", "inputArray", "outputArray"];
	var missing = new Array();
	var errorMsg = "Missing the following essential fields: ";
	var counter = 0;
	var data = JSON.stringify(data);
	eval("var data = " + data);
	console.log("from errocheck.js:" + data);
	for (var i = 0; i < fields.length; i++){ //doc or array of documents
		var field = fields[i];
		if (data.field == undefined){
			console.log("from errorcheck.js:" + data.field);
			missing[counter] = fields[i];
			counter+= 1;
		}
	}

	if (missing.length == 0) {
		return true;
	}
	else {
		for (var j = 0; j < missing.length; j++){
			errorMsg += missing[j];
			if (j < missing.length - 1){
				errorMsg += ", ";
			}
			else{
				errorMsg += ".";
			}
		}

		return errorMsg;
	}
}

		
