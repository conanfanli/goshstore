.PHONY: env test migrate

env:
	test -d .venv || virtualenv -p python3.4 .venv

test:
	python manage.py test

migrate:
	python manage.py migrate
