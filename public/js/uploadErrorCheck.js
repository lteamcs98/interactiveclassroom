/*This function checks the validity of the JSON. First it checks whether or not the file is
a JSON file. Next, it checks if the file has all the necessary fields: title, problem, functionheaders,
functionNames, inputArray, and outputArray.
*/

module.exports.uploadErrorCheck = uploadErrorCheck;

function uploadErrorCheck(data){ //data is one JSON object
	var fields = ["title", "problem", "functionHeaders", "functionNames", "inputArray", "outputArray"];
	var missing = new Array();
	var errorMsg = "Missing the following essential fields: ";
	var counter = 0;

	try{ //Check if valid JSON
		var json = JSON.parse(JSON.stringify(data));

	}
	catch (ex){
		return false;
	}

        //Iterate through each field; make sure it exists in the JSON file 
	for (var i = 0; i < fields.length; i++){ 
		var field = fields[i];

		if (!json.hasOwnProperty(fields[i])){
			missing[counter] = fields[i];
			counter+= 1;
		}
	}

	if (missing.length == 0) { //No fields are missing!
		return true;
	}
	else { //Find out which fields are missing and tell the user
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
