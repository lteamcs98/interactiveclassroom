function cmResize() {
    // Get window width and height
    var windowWidth = 800, windowHeight = 600;
    if (document.body && document.body.offsetWidth) {
        windowWidth = document.body.offsetWidth;
        windowHeight = document.body.offsetHeight;
    }
    if (document.compatMode == 'CSS1Compat' && document.documentElement &&
        document.documentElement.offsetWidth) {
        windowWidth = document.documentElement.offsetWidth;
        windowHeight = document.documentElement.offsetHeight;
    }
    if (window.innerWidth && window.innerHeight) {
        windowWidth = window.innerWidth;
        windowHeight = window.innerHeight;
    }

    // Adjust editor width and height
    editor.setSize((windowWidth - 60) * 0.66, windowHeight * 0.4);
}

cmResize();

window.onresize = function(event) {
    cmResize();
};
