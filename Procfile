web: gunicorn manage:app
worker: python -u manage.py run_worker
init: python manage.py db init
migrate: python manage.py db migrate
upgrade: python manage.py db upgrade

https://stackoverflow.com/questions/48464893/path-to-python-executable-on-heroku


