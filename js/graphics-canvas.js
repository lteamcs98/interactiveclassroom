/* graphics-canvas.js
 * Manages communication between CodeMirror console and HTML5 canvas
 */

 
var myCodeMirror = CodeMirror.fromTextArea(document.getElementById("editor"), {
    lineNumbers: true,
    mode: "text/javascript",
    matchBrackets: true,
    firstLineNumber: 0
});

var codeSnippetsCodeMirror = CodeMirror.fromTextArea(document.getElementById("codeSnippet"), {
    lineNumbers: true,
    mode: "text/javascript",
    matchBrackets: true,
    readOnly: "nocursor",
    firstLineNumber: 0
});

function codeSnippet(id)
{
    var codeSnippetEditor = CodeMirror.fromTextArea(document.getElementById(id), {
        lineNumbers: true,
        mode: "text/javascript",
        matchBrackets: true,
        readOnly: "nocursor",
        firstLineNumber: 0
    });

    $("#" + id + "Edit").click(function() {
      myCodeMirror.setValue(codeSnippetEditor.getValue());
    }); 
}

function outputSnippet(id)
{
    CodeMirror.fromTextArea(document.getElementById(id), {
        mode: "text/javascript",
        matchBrackets: true,
        readOnly: "nocursor",
        firstLineNumber: 0
    });
}