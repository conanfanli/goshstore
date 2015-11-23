.PHONY: env

env:
	test -d .venv || virtualenv -p python3.4 .venv
