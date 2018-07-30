# Reset the db migrations
# Author: setsal Lan

python manage.py migrate --fake fb_fetch zero
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
python manage.py makemigrations
python manage.py migrate --fake-initial
