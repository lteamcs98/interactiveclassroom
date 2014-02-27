var yaml = require('yaml-front-matter');
exports.parseMarkdown = parseMarkdown; 
//takes in a block of content data: 
function parseMarkdown(content){
	var lines = content.split('\n');
	var mdDocs = new Array(); //array of markdown docs
	//var jsonDocs = new Array();
	var mdDoc = "";//store current markdown doc
	var numDoc = 0;

	for (var i = 0; i < lines.length; i++) {
		if (lines[i][0] == "#") {
			mdDocs[numDoc] = mdDoc; 
			mdDoc = "";
			numDoc += 1;
		}
		else {
			mdDoc += lines[i] + "\n";
		}
	}
	
	return mdDocs;
}





	
		
