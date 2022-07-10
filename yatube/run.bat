coverage run --source='posts,users,about' manage.py test -v 2
coverage report
coverage html
python manage.py test