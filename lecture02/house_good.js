// Program to draw a simple house
// cs1 example of use of commenting and whitespace
// author Devin Balkcom
// July, 2011

// Function to draw a house.
function drawHouse(){
	//draw the lawn
	canvas.fillStyle = "#006400"; //dark green
	canvas.fillRect(0, 100, 300, 50);

	//draw the main square part of the house
	canvas.fillStyle = "#8B4513"; //brown
	canvas.fillRect(100, 50, 100, 80);

	//draw the roof
	canvas.fillStyle = "#8B0000";//red
	canvas.fillRect(90,30, 120,20);

	// draw the door
	canvas.fillStyle = "#B8860B"; // light brown
	canvas.fillRect(140, 80, 20, 50);

	//draw the doorknob
	canvas.fillStyle = "#000000"; // black
	canvas.fillRect(150, 100, 5, 5);
}

drawHouse();