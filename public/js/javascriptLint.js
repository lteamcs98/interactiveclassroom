// CodeMirror JavaScript Linter
// Modified for Dartmouth CS98 Interactive Classroom Project by Michelle Shu

(function() {
  "use strict";
  // declare global: JSHINT

  var bogus = [ "Dangerous comment" ];

  var warnings = [ "Missing semicolon",
  	" was used before it was defined",
	" is already defined", 
	"The array literal notation [] is preferrable", 
	"The object literal notation {} is preferrable", 
	"Unexpected space ",
	"Missing space ", 
	"Bad line breaking before ",
	" to have an indentation at ", 
	"Unexpected use of ",
	"Bad operand", 
	" is a function", 
	"Missing name in function declaration", 
	"Inner functions should be listed", 
	"Unreachable", 
	"Expected an assignment or function call and instead saw an expression", 
	"Unnecessary semicolon", 
	"Missing semicolon", 
	" used out of scope", 
	" is not allowed", 
	" is out of scope", 
	"Did you mean to return a conditional instead of an assignment?", 
	"Unexpected comma", 
	"Expected a string and instead saw ", 
	"Mixed double and single quotes", 
	"Unclosed string", 
	" and instead saw "];

  var errors = [ "Unexpected early end of program", 
  	 " has already been declared", 
	 " is initialized to 'undefined'", 
	 "Attempting to override ",
	 "Unclosed regular expression", 
	 "Invalid regular expression", 
	 "Unclosed comment", 
	 "Unbegun comment", 
	 "Unmatched ", 
	 " to match ", 
	 "Line breaking error", 
	 "Missing ':' on a case clause", 
	 "Missing '}' to match '{' ", 
	 "Missing ']' to match '[' ", 
	 "Illegal comma", 
	 "Unclosed string",
	 "Expected an identifier and instead saw ", 
	 "Bad assignment", 
	 "Expected a small integer or 'false' and instead saw ", 
	 "Expected an operator and instead saw ", 
	 "Missing property name", 
	 "Expected to see a statement and instead saw a block", 
	 " was not declared properly", 
	 " is already defined and can't be redefined", 
	 "Invalid for each loop", 
	 " cannot be named "];

  function validator(text, options) {
    JSHINT(text, options);
    var errors = JSHINT.data().errors, result = [];
    if (errors) parseErrors(errors, result);
    return result;
  }

  CodeMirror.registerHelper("lint", "javascript", validator);
  CodeMirror.javascriptValidator = CodeMirror.lint.javascript; // deprecated

  function cleanup(error) {
    // All problems are warnings by default
    fixWith(error, warnings, "warning", true);
    fixWith(error, errors, "error");

    return isBogus(error) ? null : error;
  }

  function fixWith(error, fixes, severity, force) {
    var description, fix, find, replace, found;

    description = error.description;

    for ( var i = 0; i < fixes.length; i++) {
      fix = fixes[i];
      find = (typeof fix === "string" ? fix : fix[0]);
      replace = (typeof fix === "string" ? null : fix[1]);
      found = description.indexOf(find) !== -1;

      if (force || found) {
        error.severity = severity;
      }
      if (found && replace) {
        error.description = replace;
      }
    }
  }

  function isBogus(error) {
    var description = error.description;
    for ( var i = 0; i < bogus.length; i++) {
      if (description.indexOf(bogus[i]) !== -1) {
        return true;
      }
    }
    return false;
  }

  function parseErrors(errors, output) {
    for ( var i = 0; i < errors.length; i++) {
      var error = errors[i];
      if (error) {
        var linetabpositions, index;

        linetabpositions = [];

        // This next block is to fix a problem in jshint. Jshint
        // replaces
        // all tabs with spaces then performs some checks. The error
        // positions (character/space) are then reported incorrectly,
        // not taking the replacement step into account. Here we look
        // at the evidence line and try to adjust the character position
        // to the correct value.
        if (error.evidence) {
          // Tab positions are computed once per line and cached
          var tabpositions = linetabpositions[error.line];
          if (!tabpositions) {
            var evidence = error.evidence;
            tabpositions = [];
            // ugggh phantomjs does not like this
            // forEachChar(evidence, function(item, index) {
            Array.prototype.forEach.call(evidence, function(item,
                                                            index) {
              if (item === '\t') {
                // First col is 1 (not 0) to match error
                // positions
                tabpositions.push(index + 1);
              }
            });
            linetabpositions[error.line] = tabpositions;
          }
          if (tabpositions.length > 0) {
            var pos = error.character;
            tabpositions.forEach(function(tabposition) {
              if (pos > tabposition) pos -= 1;
            });
            error.character = pos;
          }
        }

        var start = error.character - 1, end = start + 1;
        if (error.evidence) {
          index = error.evidence.substring(start).search(/.\b/);
          if (index > -1) {
            end += index;
          }
        }

        // Convert to format expected by validation service
        error.description = error.reason;// + "(jshint)";
        error.start = error.character;
        error.end = end;
        error = cleanup(error);

        if (error)
          output.push({message: error.description,
                       severity: error.severity,
                       from: CodeMirror.Pos(error.line - 1, start),
                       to: CodeMirror.Pos(error.line - 1, end)});
      }
    }
  }
})();
