/* graphics-canvas.js
 * Manages communication between CodeMirror console and HTML5 canvas
 */


$(document).ready(function() {
	$("#compile-button").click(evalCode);
});

var evalCode = function() {
	var canvas = $("#canvas")[0].getContext("2d");
	// Clear the canvas
	canvas.fillStyle="#FFFFFF";
	canvas.fillRect(0, 0, $("#canvas")[0].width, $("#canvas")[0].height);
	var code = $("#console").val();
	eval(code);
}