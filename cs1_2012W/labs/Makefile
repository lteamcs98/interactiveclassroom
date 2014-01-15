HTML = lab_assignments.html
# pong/lab_pong.html gravity/lab_gravity.html quicksort/lab_quicksort.html bfs/lab_bfs.html crawler/lab_crawler.html

all:  $(HTML)
    
%.html: %.txt 
	pandoc -o $@ -B ../header.html  $<

clean:  
	rm -f $(HTML)