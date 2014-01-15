
HTML = lecture01/lecture01.html
# lecture02/lecture02.html lecture03/lecture03.html lecture04/lecture04.html lecture05/lecture05.html lecture06/lecture06.html lecture07/lecture07.html lecture08/lecture08.html lecture09/lecture09.html lecture10/lecture10.html lecture11/lecture11.html lecture12/lecture12.html lecture13/lecture13.html lecture14/lecture14.html lecture15/lecture15.html lecture16/lecture16.html lecture17/lecture17.html lecture18/lecture18.html lecture19/lecture19.html lecture20/lecture20.html lecture21/lecture21.html lecture22/lecture22.html lecture23/lecture23.html lecture24/lecture24.html lecture25/lecture25.html

all:  $(HTML)

%.html: %.txt Makefile
	pandoc -o $@ -B ../header.html  $<

clean:  
	rm -f $(HTML)