// We must make sure we have all the right wrapper functions for this to work:
// clear, draw_circle, and start_graphics.

function main(){
    
    clear();
    
    draw_circle(125, 100, 50);
    draw_circle(275, 100, 50);
}

start_graphics(main());
