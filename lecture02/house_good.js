// Program to draw a simple house
// cs1 example of use of commenting and whitespace
// author Devin Balkcom (adapted from python to javascript by L'team)
// Winter, 2014

// Function to draw a house.
function drawHouse(){
	//draw the lawn
	processing.fill(0,128,0); //dark green
	processing.rect(0, 300, 400, 100);

	//draw the main square part of the house
	processing.fill(128, 102, 51); //brown
	processing.rect(200, 250, 130, 100);

	//draw the roof
	processing.fill(255,0,0);//red
	processing.triangle(200, 250, 330, 250, 265, 20);

	// draw the door
	processing.fill(153,128,77); // light brown
	processing.rect(280, 310, 25, 40);

	//draw the doorknob
	processing.fill(0,0,0); // black
	ellipse(300, 330, 3,3);
}

//set the size of the window
size(400,400);

drawHouse();