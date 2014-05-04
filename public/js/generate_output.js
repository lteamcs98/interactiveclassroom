module.exports.generateOutputArray = generateOutputArray;

//This should return an array of whatever (strings, integers)
function getOutput(solution, functionName, inputs){ //solution is a string of js code
	var outputs = new Array();
	var functionTag = "{'functionName':" + functionName + ",";
	eval(solution);

	for (var j = 0; j < inputs.length; j++){
		var output = new Array();
		output[0] = eval(functionName +'.apply(null, [inputs[j]])');
		outputs[j] = output;
	}

	var json = JSON.stringify(outputs);
	functionTag += "'outputs':";
	functionTag += json;
	return functionTag;
}

function getInputs(json){
	var inputs =  new Array();

	for (var i = 0; i < json.functionNames.length; i++){
		inputs[i] = json.inputArray[i].inputs;
	}

	return inputs;
}

function generateOutputArray(json){
	var outputArray = "'outputArray': [";
	//inputArray is not in array form exactly...
	var inputs = getInputs(json);

	for (var i = 0; i < json.functionNames.length; i++){
		var output = "" + getOutput(json.solutions[i], json.functionNames[i], inputs[i]) + "}";
		if (i < json.functionNames.length - 1){
			output+= ",";
		}
		outputArray += output;
	}

	outputArray += "]";
	outputArray = JSON.stringify(outputArray);

	return outputArray;
}
