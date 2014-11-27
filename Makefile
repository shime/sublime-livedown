all:
	zip -r build/Livedown.sublime-package . -x *.git* -x *.pyc -x Makefile
