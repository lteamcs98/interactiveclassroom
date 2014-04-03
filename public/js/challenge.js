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

var editor = CodeMirror.fromTextArea(document.getElementById("codeEditor"),
{
	lineNumbers: true,
	mode: "javascript",
	gutters: ["CodeMirror-lint-markers"],
	lint: true,
	theme: "light-table"
});

editor.setSize(540, 300);

function test(str1, str2, str3)
{
	console.log(str1);
	console.log(str2);
	console.log(str3);
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

		$('#outputBox').append('<p class="functionTitle">' + functionName + '</p>');

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
			var output = eval(functionName+'(inputs[evalIterator])');
			if(arraysEqual(output, outputs[evalIterator])) {
				correct += 1.0;
				$('#outputBox').append('<p class="correctResult">Test ' + evalIterator + ' passed</p>');
			} else {
				failedTests.push(evalIterator);
				$('#outputBox').append('<p class="incorrectResult">Test ' + evalIterator + ' failed<br />' +
										'Input: ' + inputs[evalIterator] + '<br />' +
										'Your output: ' + output + '<br />' +
										'Correct output: ' + outputs[evalIterator] + '</p>');
			}
		}
		return [total, correct, failedTests];
}

$('#submitButton').click(function() {
	$('#outputBox').html('<p class="challengeTitle">Results</p>');

	var testIndex = document.getElementById("codeUnitList").selectedIndex;
	var testAll = (testIndex === 0);
	var functions = new Array();
	if (testAll)
	{
		functions = functionNames;
	} else
	{
		functions.push(document.getElementById("codeUnitList").options[testIndex].value);
	}

	totalTests = 0;
	correctTests = 0;
	var failedTests = new Array();
	for(var i in functions)
	{
		result = evaluateFunction(functions[i]);
		if(typeof result == 'number')
		{
			continue;
		}
		totalTests += result[0];
		correctTests += result[1];
		failedTests.push({functionName: functions[i], failedTests: result[2]});
	}
	if(totalTests > 0)
	{
		var percent = (100.0 * correctTests / totalTests);
		$('#outputBox').append('<p class="challengeTitle">' + percent + "% Correct</p>");
	}
	else 
	{
		$('#outputBox').append('<p class="challengeTitle">No results to display</p>');
	
	}
});