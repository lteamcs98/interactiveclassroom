
function spongebob(width, height){
smooth(); //smooths the drawing strokes

size(width, height);

//square body
noStroke();
fill(253, 235, 29); //yellow
rect(0, 0, width, height);
stroke(0, 0, 0);

//teeth
fill(255,255,255); //white
rect(width/2, height/2 + 40, 20, 25);
rect(width/2 - 25, height/2 + 40, 20, 25);

//smile
fill(253, 235, 29); //yellow
stroke(0,0,0); //black
ellipse(width/2, height/2, width - 90, 100);
fill(253, 235, 29); //yellow
noStroke();
ellipse(width/2, height/2 - 10, width - 90, 100);
stroke(0,0,0); //black

//eyelashes
strokeWeight(4);
//left eye
line(width/3, height/3, width/3 - 20, height/3 - 50); //left
line(width/3, height/3, width/3, height/3 - 50); //center
line(width/3, height/3, width/3 + 20, height/3 - 50); //right

//right eye
line(width - width/3, height/3, width - width/3 - 20, height/3 - 50); //left
line(width - width/3, height/3, width - width/3, height/3 - 50); //center
line(width - width/3, height/3, width - width/3 + 20, height/3 - 50); //right
strokeWeight(1);

//eyes

//sclera
fill (255, 255, 255); //white
var sclera = 85; //sclera
ellipse(width/3, height/3, sclera, sclera); 
ellipse(width - width/3, height/3, sclera, sclera);

//iris
var iris = 30;
fill(53,190,255); //light blue
ellipse(width/3, height/3, iris, iris);
ellipse(width - width/3, height/3, iris, iris);

//pupil
var pupil = 15;
fill(0,0,0); //black
ellipse(width/3, height/3, pupil, pupil);
ellipse(width - width/3, height/3, pupil, pupil);

//nose
strokeWeight(2);
fill(253, 235, 29); //yellow
ellipse(width/2, height/2 - 20, 20, 30);
noStroke();
ellipse(width/2, height/2, 20, 20);
 
//cheeks
strokeWeight(2);
stroke(211, 33, 19); //red
fill(253, 235, 29); //yellow
ellipse(width/3 - 35, height/3 + 35, 35, 30); 
ellipse(width - width/3 + 35, height/3 + 35, 35, 30); 
noStroke();
ellipse(width/3 - 35, height/3 + 37, 35, 30); 
ellipse(width - width/3 + 35, height/3 + 37, 35, 30); 

//freckles
fill(211, 33, 19); //red
ellipse(width/3 - 35, height/3 + 40, 2, 2); 
ellipse(width/3 - 25, height/3 + 30, 2, 2); 
ellipse(width/3 - 45, height/3 + 30, 2, 2); 
ellipse(width - width/3 + 35, height/3 + 40, 2, 2);
ellipse(width - width/3 + 25, height/3 + 30, 2, 2); 
ellipse(width - width/3 + 45, height/3 + 30, 2, 2);

//sponge holes
noStroke();
fill(112, 176, 17); //yellow green
ellipse(40, 30, 30, 20);
ellipse(30, 50, 15, 13);
ellipse(width - 30, 20, 15, 10);
ellipse(50, height - 50, 20, 20);
ellipse(width - 45, height - 30, 20, 25);
ellipse(width - 30, height - 50, 12, 15);

}

spongebob(250, 250);