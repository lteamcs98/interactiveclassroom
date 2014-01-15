HTML = short_assignments.html logo/sa_logo.html sketch/sa_sketch.html rich/sa_rich.html stringart/sa_stringart.html chalkboard/sa_chalkboard.html movingblocks/sa_movingblocks.html timer/sa_timer.html binarysearch/sa_binarysearch.html
# insertion/sa_insertion.html clock/sa_clock.html adventure/sa_adventure.html

all:  $(HTML)
    
%.html: %.txt 
	pandoc -o $@ -B ../header.html  $<

clean:  
	rm -f $(HTML)