var yaml = require('yaml-front-matter');
//takes in a block of content data: 
function parseMarkdown(content){
	var lines = content.split('\n');
	var mdDocs = new Array(); //array of markdown docs
	var jsonDocs = new Array();
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
	
	//Convert markdown docs to JSON docs
	for (var i = 0; i < mdDocs.length; i++) {
		var jsonDoc = yaml.loadFront(mdDocs[i]);
		jsonDocs[i] = jsonDoc;
		console.log(jsonDoc);
	}

	return jsonDocs;
}

/*
var test = "---\n";
test += "title: That Night \n";
test += "author: Alice McDermott \n";
test += "characters: \n";
test += "- Rick \n";
test += "- Sheryl \n";
test += "--- \n";
test += "#\n";
test += "---\n";
test += "title: The Round House\n";
test += "author: Louise Erdrich\n";
test += "characters:\n";
test += "- Joe\n";
test += "- Linden Lark\n";
test += "- Geraldine\n";
test += "---\n";
test += "#\n";

parseMarkdown(test); */




	
		
