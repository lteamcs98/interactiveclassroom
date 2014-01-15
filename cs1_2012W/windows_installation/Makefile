HTML = windows_installation.html
all:  $(HTML)

%.html: %.txt ../header.html
	pandoc -o $@ -B ../header.html $<

clean:  
	rm -f $(HTML)