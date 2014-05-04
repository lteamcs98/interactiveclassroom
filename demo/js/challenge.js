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

var editor = CodeMirror.fromTextArea(document.getElementById("editor"),
{
	lineNumbers: true,
	mode: "javascript",
	gutters: ["CodeMirror-lint-markers"],
	lint: true,
	theme: "light-table"
});

editor.setSize(540, 300);

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


		var inputs = inputArray.inputs;
		var outputs = outputArray.outputs;

		var total = inputs.length;
		var correct = 0.0;


		for (var i = 0; i < 2; i++)
		{
			var output = eval(findMax(inputs[i]));

			if (output == outputs[i]) {
				correct += 1.0;
				$('#results').append('<p class="correctResult">Test ' + i + ' passed</p><br>');
			} else {
				failedTests.push(i);
				$('#results').append('<p class="incorrectResult">Test ' + i + ' failed<br />' +
										'Input: ' + inputs[i] + '<br />' +
										'Your output: ' + output + '<br />' +
										'Correct output: ' + outputs[i] + '</p><br>');
			}
		}

		return [total, correct, failedTests];
}
