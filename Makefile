VENV = $(HOME)/.virtualenvs/ecommerce-api/bin

server:
	sudo systemctl start postgresql.service;
	cd src && $(VENV)/python manage.py migrate && $(VENV)/python manage.py runserver;

makemigrations:
	cd src && $(VENV)/python manage.py makemigrations;
