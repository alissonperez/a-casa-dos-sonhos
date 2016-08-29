setup_db:
	./manage.py migrate
	./manage.py populate

serve:
	./manage.py runserver

test:
	./manage.py test
