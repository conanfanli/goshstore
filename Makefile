.PHONY: env test migrate

env:
	test -d .venv || virtualenv -p python3.4 .venv

test:
	coverage run ./manage.py test && coverage report -m --omit=*/urls.py,*/settings.py,*/__init__.py,setup.py --include=goshstore/*

migrate:
	python manage.py migrate
