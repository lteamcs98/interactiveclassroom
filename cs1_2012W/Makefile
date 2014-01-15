WEBDIR = cs1@galehead.cs.dartmouth.edu:~/public_html

HTML = exams.html syllabus.html schedule.html software.html index.html
DOCS = Questionnaire.doc laptop-agreement.doc section-times.doc
DIRS = lectures labs shortassign mac_installation windows_installation


all:  $(HTML) subdirs

index.html: syllabus.html
	cp syllabus.html index.html

subdirs:    
	set -e; for d in $(DIRS); do make -C $$d ; done

%.html: %.txt
	pandoc -o $@ -B header.html $<

clean:  
	rm -f $(HTML)
	set -e; for d in $(DIRS); do make -C $$d clean; done

install: 
	rsync -aPpe ssh . $(WEBDIR)
