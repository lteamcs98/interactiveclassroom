/* graphics-canvas.js
 * Manages communication between CodeMirror console and HTML5 canvas
 */

var myCodeMirror = CodeMirror.fromTextArea(document.getElementById("console"), {
    lineNumbers: true,
    mode: "text/javascript",
    matchBrackets: true,
    firstLineNumber: 0
});