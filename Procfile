release: python manage.py makemigrations && python manage.py migrate
web: gunicorn planner-drf-api.wsgi