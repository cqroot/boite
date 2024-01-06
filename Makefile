PROC_NAME = boite

.PHONY: build
build: clean
	pyinstaller -w '$(PROC_NAME)/__main__.py' -n '$(PROC_NAME)'

.PHONY: run
run:
	env PYTHONDONTWRITEBYTECODE=1 python -m '$(PROC_NAME)'

.PHONY: clean
clean:
	rm -rf '$(CURDIR)/build/'
	rm -rf '$(CURDIR)/dist/'
	find '$(CURDIR)/$(PROC_NAME)/' -type d -prune -name __pycache__ -exec rm -rf {} \;
	find '$(CURDIR)/$(PROC_NAME)/' -type f        -name *.pyc       -exec rm -f  {} \;

.PHONY: requirements
requirements:
	pip freeze | grep -iE '^pyside6==|^pyinstaller==' > requirements.txt
