/* Capture JavaScript console output and reroute to console box on interactive
	challenge */

var logOfConsole = [];

var _log = console.log,
	_warn = console.warn,
	_error = console.error;

function outputArguments(arguments, type)
{
	outputBox = document.getElementById('console');
	for(var i in arguments)
	{
		if(type == 0)
		{
			outputBox.innerHTML += '<p class="consoleLog">'+(arguments[i])+'</p>';
		}
		else if (type == 1)
		{
			outputBox.innerHTML += '<p class="consoleWarn">'+(arguments[i])+'</p>';
		}
		else
		{
			outputBox.innerHTML += '<p class="consoleError">'+(arguments[i])+'</p>';
		}
	}
}

console.log = function() {
	outputArguments(arguments, 0);
	logOfConsole.push({method: 'log', arguments:arguments});
	return _log.apply(console, arguments);
};

console.warn = function() {
	outputArguments(arguments, 1);
	logOfConsole.push({method: 'warn', arguments: arguments});
	return _warn.apply(console, arguments);
};

console.error = function() {
	outputArguments(arguments, 2);
	logOfConsole.push({method: 'error', arguments: arguments});
	return _error.apply(console, arguments);
};

window.onerror = function (msg, url, line) {
    console.error("Console Error: '" + msg + "' from " + url + ":" + line);
    return true; // same as preventDefault
};
