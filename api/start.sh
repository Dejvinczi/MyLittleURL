#!/bin/sh

pip install -r requirements.txt 

python manage.py migrate

if [ -z "$(python manage.py shell -c 'from django.contrib.auth import get_user_model; print(get_user_model().objects.filter(username="'"$DJANGO_SUPERUSER_USERNAME"'").exists())')" ]; then
    echo "** Creating superuser **";
    python manage.py createsuperuser --no-input;
fi

if [ $DEBUG ]; 
then
    pip install debugpy -t /tmp
    python /tmp/debugpy --listen $API_HOST:5678 manage.py runserver $API_HOST:$API_PORT
else
    python manage.py runserver $API_HOST:$API_PORT
fi
