var i = 0;

// set up
background(255);
size(750, 250);
smooth();
frameRate(30);
strokeWeight(12);

// draw
function something()
{
    stroke(random(0, 50), random(0, 255), random(0, 255), 100);
    line(i, 0, random(0, width()), height());
    line(width()-i, 0, random(0, width()), height());
    line(i, height(), random(0, width()), 0);
    line(width()-i, height(), random(0, width()), 0);            
    if(i < width())
    {
        i = i + 1;
    } else
    {
        i = 0;
    }
    ellipse(random(0, width()), random(0, height()), 25, 25);
  	triangle(0, 0, width(), 0, width()/2, height()/2);
  	triangle(0, height(), width(), height(), width()/2, height()/2);
}

var id = cs1SetInterval(something, 100);