git clone https://github.com/Rohith-chintham/college-django.git

cd college-django

python -m venv venv

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

http://127.0.0.1:8000/
