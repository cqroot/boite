PROC_NAME = boite

.PHONY: build
build:
	pyinstaller -w '$(PROC_NAME)/__main__.py' -n '$(PROC_NAME)'
	# pyinstaller '$(PROC_NAME).spec'

.PHONY: run
run:
	env PYTHONDONTWRITEBYTECODE=1 python -m '$(PROC_NAME)'

.PHONY: clean
clean:
	rm -rf '$(CURDIR)/build/'
	rm -rf '$(CURDIR)/dist/'

.PHONY: requirements
requirements:
	pip freeze | grep -iE '^pyside6==|^pyinstaller==' > requirements.txt
