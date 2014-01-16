/* processing-wrapper.js
 * A wrapper class for processing.js that eliminates the use of the Processing instance for users
 */
 
// call compileInput when the compile button is clicked
$(document).ready(function() {
	$("#compile-button").click(processInput);
});

var canvasCode, textOutput;

// keeps track of the current processing instance (instances are created when a sketch is compiled)
var currentProcessingInstance = null;

function print(str)
{
	console.log("Called");
	$('#output').append(str);
	$('#output').append("<br />");
}

// Draw on canvas and type to text output area.
function processInput()
{	
    // store the user's code from the code mirror editor
    var code = myCodeMirror.getValue();
    
    // grab the canvas element in the html
    var canvas = document.getElementById("canvas1");
            
    // attaching the wrapperFunction function to the canvas
    // begin a new sketch
    currentProcessingInstance = new Processing(canvas, wrapperFunction);
}
    
// this function creates an instance of the wrapper class and evaluates the user code given
function wrapperFunction(processing)
{
    var class_instance = new wrapperClass(processing, myCodeMirror.getValue());
    // run the code
    class_instance.evalCode();
}
    
// this wrapper classes exposes functionality from process.js (while abstracting away some of the object-oriented syntax for cs1 students)
// it also wraps some basic JavaScript functions such as setInterval
function wrapperClass(processing, code)
    {     
        // this processing instance
        this.processing = processing;
        
        // the code provided by the user
        this.code = code;
        
        // this array keeps track of all the interval ids that were created in the user code
        var interval_ids = [];
        
        // add callbacks so that the sketch will be stopped 
        $("#compile-button").click(stopSketch);
        $("#stop-button").click(stopSketch);
        
        console.log('initialized wrapper class');
        
        // draw an ellipse
        function ellipse(x, y, h, w)
        {
            processing.ellipse(x, y, h, w);
        }
        
        // draw a triangle between the three points with the given coordinates
        function triangle(x1, y1, x2, y2, x3, y3)
        {
            processing.triangle(x1, y1, x2, y2, x3, y3)
        }
        
        // draw a rectangle with a top left corner coordinate (x,y) and the given width and height
        function rect(x, y, width, height)
        {
            processing.rect(x, y, width, height);
        }
        
        // generate a random number from the given range
        function random(min, max)
        {
            return processing.random(min, max);
        }
        
        // set the background of the canvas to the appropriate color
        function background(color)
        {
            processing.background(color);
        }
        
        // set the size of the canvas
        function size(width, height)
        {
            processing.size(width, height);
        }
        
        // smooth the drawing strokes
        function smooth()
        {
            processing.smooth();
        }
        
        // set the frame rate for the built-in draw function
        function frameRate(rate)
        {
            processing.frameRate(rate);
        }
        
        // set the stroke width
        function strokeWeight(weight)
        {
            processing.strokeWeight(weight);
        }
        
        // set the stroke color with the appropriate RGB values and opacity
        function stroke(r, g, b, alpha)
        {
            processing.stroke(r, g, b, alpha);
        }

        function noStroke()
        {
            processing.noStroke();
        }
        
        function fill(r, g, b)
        {
            processing.fill(r, g, b);
        }
        
        // draw a line between the points with the given coordinates
        function line(x1, y1, x2, y2)
        {
            processing.line(x1, y1, x2, y2);
        }
                
        // get the width of the canvas
        function width()
        {
            return processing.width;
        }
        
        // get the height of the canvas
        function height()
        {
            return processing.height;
        }
               
        // tell processing not to loop on the draw function
        function noLoop()
        {
            processing.noLoop();
        }
        
        // tell processing to loop on the draw function
        function loop()
        {
            processing.loop();
        }
                
        // exit a processing sketch
        function exit()
        {
            processing.exit();
        }
        
        // a wrapper for the JavaScript setInterval function so that we can keep track of IDs to clear 
        // when the sketch is killed
        function cs1SetInterval(fn, delay)
        {
            console.log('setting interval');
            // set the interval
            var id = setInterval(fn, delay);
            
            // store the ID in an array of all IDs created during this sketch
            interval_ids.push(id);
            console.log(id);
        }

        // stop the current sket that is running (if one exists)
        function stopSketch()
        {          
            console.log('stopping sketch!');
            // loop through the array of IDs and clear all intervals associated with them
            for (var i = 0; i < interval_ids.length; i++) {
                clearInterval(interval_ids[i]);
            }

            // exit the current sketch
            exit();
            
            /*
            // get the canvas
            var canvas = $("#canvas1")[0].getContext("2d");
            
            // Clear the canvas
            canvas.fillStyle="#FFFFFF";
            canvas.fillRect(0, 0, $("#canvas1")[0].width, $("#canvas1")[0].height);
            */
        }
        
        // evaluate/run the code the user writes 
        this.evalCode = function()
        {
            stopSketch();
            noLoop();
			
			console.log(this.code);
			
            // run their code
            eval(this.code);
        }        
    }
    
/*
// sketch code
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

var id = cs1SetInterval(something, 1000);
*/