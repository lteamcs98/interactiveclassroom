// The load function can be moved somewhere else once we've wrapped everything.
function load(url)
{
    // Adding the script tag to the head as suggested before
    var head = document.getElementsByTagName('head')[0];
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = url;

    // Fire the loading
    head.appendChild(script);
}

load("simplefucntions.js");

print_sqrt(4);
print_sqrt(9);
