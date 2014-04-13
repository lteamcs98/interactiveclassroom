module.exports.generateOutputArray = generateOutputArray;

//This should return an array of whatever (strings, integers) 
function getOutput(solution, functionName, inputs){ //solution is a string of js code
	var outputs = new Array();
	var functionTag = "{'functionName':" + functionName + ",";
	//console.log(functionTag);
	eval(solution);
	//console.log("The inputs:" + inputs);
	for (var j = 0; j < inputs.length; j++){
		var output = new Array();
		//console.log("The input for function:" + functionName + "is:" + inputs[j][0]);
		output[0] = eval(functionName +'.apply(null, [inputs[j]])');
		//console.log(output);
		outputs[j] = output;
		//console.log(outputs);
	}
	
	var json = JSON.stringify(outputs);
	functionTag += "'outputs':";
	functionTag += json;
	//console.log(functionTag);

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
		console.log(output);
		outputArray += output;
	}

	outputArray += "]";
	outputArray = JSON.stringify(outputArray);

	return outputArray;
}
	
/*
var test = "function addThree(x){ return x + 3; }";
var test2 = "function addFour(y) { return y + 4; }";
var test3 = "function addFive(x) { return x + 5; }";
var solutions = [test, test2, test3];
var functionNames = ["addThree", "addFour", "addFive"];
var inputArrays = [[[1], [2], [3]], [[0], [1], [2]], [[3], [4], [5]]];

console.log(generateOutputArray(solutions, functionNames, inputArrays));*/

