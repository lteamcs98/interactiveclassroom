function drawPineappleHouse()
{
	//draw the sea
	fill(49, 230, 255); //light blue
	rect(0, 0, 400, 400);

	//draw the pineapple
	fill(255, 160, 50); // light orange
	ellipse(275, 200, 170, 250);

	//draw the sand
	fill(230, 235, 156); //tan
	rect(0, 300, 400, 100);

	//draw the leaves
	fill(139, 195, 26); // light green
	triangle(225, 100, 325, 100, 200, 35);
	fill(0, 84, 0); // dark green
	triangle(225, 100, 325, 100, 350, 35);
	fill(91, 156, 14); //medium green
	triangle(225, 100, 325, 100, 275, 35);

	//draw a door
	fill(48, 133, 216); // blue
	rect(250, 230, 50, 70);

	//draw the windows
	ellipse(230, 160, 30, 40);
	ellipse(330, 240, 20, 30);

	//draw the chimney
	rect(350, 150, 30, 10);
	rect(370, 130, 10, 30);

	//draw the bubbles
	fill(255, 255, 255);// white
	ellipse(375, 100, 20, 20);
	ellipse(380, 70, 10, 10);

	//draw the walkway
	fill(98, 123, 130); //grey
	rect(250, 300, 50, 100);
	triangle(250, 300, 200, 400, 250, 400);
	triangle(300, 300, 300, 400, 350, 400);
}
size(400, 400);
noStroke();
drawPineappleHouse();
