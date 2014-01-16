//basic cs1 example of use of drawing shapes, layering order, RGB colors
//Exercise to draw a stoplight.

function stoplight(){
  size(100,200);  
  
  //base  
  fill(0,0,0);
  ellipse(50,170,50,20);
  
  //pole
  fill(255,255,255);
  rect(45,120,10,50);
   
  //sign
  fill(50,50,50);
  rect(25,25,50,100);
  
  //stop
  fill(128,0,0);
  stroke(255,0,0);
  ellipse(50,50,20,20);
  
  //slow
  fill(128,128,0,128);
  stroke(255,255,0);
  ellipse(50,75,20,20);
  
  //go
  fill(0,128,0);
  stroke(0,255,0);
  ellipse(50,100,20,20);
    
  //flashes
  strokeWeight(5);
  line(25,100,35,100);  // left mid
  line(65,100,75,100);  // right mid
  line(25,85,35,90);    // left up
  line(25,115,35,110);  // left down 
  line(65,90,75,85);    // right up
  line(65,110,75,115);  // right down
  
}

stoplight();
