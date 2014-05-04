/* Handles callback for Submit button on challenges; test if submitted code
	gives correct output */

function arraysEqual(a, b)
{
	if(typeof a != "object" && typeof b != "object")
	{
		return a==b;
	}

	if (a === b) return true;
	if (a == null || b == null) return false;
	if (a.length != b.length) return false;

	// If you don't care about the order of the elements inside
	// the array, you should sort both arrays here.

	for (var i = 0; i < a.length; ++i)
	{
		if (a[i] !== b[i]) return false;
	}
	return true;
}

function addFunctionOptions(functionNames)
{
	var select = document.getElementById("codeUnitList");
	for(var i in functionNames)
	{
		var name = functionNames[i];
		var option = document.createElement("option");
		option.text = name;
		option.id = name;
		select.add(option);
	}
}

function evaluateFunction(functionName) {
		eval(editor.getValue());
		if(typeof eval(functionName) != 'function')
		{
			console.error('Console Error: Please declare the following function: ' + functionName);
			return -1;
		}

		$('#results').append('<p>' + functionName + '</p>');

		var inputs = new Array();
		var outputs = new Array();
		var failedTests = new Array();

		for(var inputIterator in inputArray)
		{
			if(functionName == inputArray[inputIterator].functionName)
			{
				inputs = inputArray[inputIterator].inputs;
			}
		}
		for(var outputIterator in outputArray)
		{
			if(functionName == outputArray[outputIterator].functionName)
			{
				outputs = outputArray[outputIterator].outputs;
			}
		}

		var total = inputs.length;
		var correct = 0.0;

		for(var evalIterator in inputs)
		{
			//var output = eval(functionName+'(inputs[evalIterator])');
			var output = eval(functionName+'.apply(null, inputs[evalIterator])');

			if(arraysEqual(output, outputs[evalIterator])) {
				correct += 1.0;
				$('#results').append('<p class="correctResult">Test ' + evalIterator + ' passed</p><br>');
			} else {
				failedTests.push(evalIterator);
				$('#results').append('<p class="incorrectResult">Test ' + evalIterator + ' failed<br />' +
										'Input: ' + inputs[evalIterator] + '<br />' +
										'Your output: ' + output + '<br />' +
										'Correct output: ' + outputs[evalIterator] + '</p><br>');
			}
		}

		return [total, correct, failedTests];
}
