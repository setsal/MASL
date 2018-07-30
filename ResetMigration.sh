# Reset the db migrations
# Author: setsal Lan

if [ $# = 1 ];then
    python manage.py migrate --fake $1 zero
    find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
    find . -path "*/migrations/*.pyc"  -delete
    python manage.py makemigrations
    python manage.py migrate --fake-initial
else
    echo "Usage: sh ResetMigration.sh [your app]"
    exit
fi
