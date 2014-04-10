module.exports.getOutputs = getOutputs;

//This should return an array of whatever (strings, integers) 
function getOutputs(solution, functionNames, inputs){ //solution is a string of js code
	var outputs = new Array();
	eval(solution);
	eval("inputs = " + inputs);
	console.log(inputs);
	eval("functionNames =" + functionNames);

	for (var i = 0; i < functionNames.length; i++){
		var output = new Array();
		for (var j = 0; j < inputs[i].length; j++){
			console.log(functionNames[i]);
			var temp = eval(functionNames[i] +'.apply(null, [inputs[i][j]])');
			output[j] = temp;
		}
		outputs[i] = output;
	}

	return outputs;
}

var test = "function addThree(x){ return x + 3; }";
var testInputs = "[[1, 2, 3]]";
var functionNames = "['addThree']";

console.log(getOutputs(test, functionNames,  testInputs));
