# django-code-along

## ⚠️⚠️⚠️ DO NOT FORK ⚠️⚠️⚠️

```
cd Desktop
cd seir-7-25/unit-03
git clone git@git.generalassemb.ly:SEIR-7-25/django-code-along-day-01.git
cd django-code-along-day-01

pip3 install virtualenv
python3 -m venv env
source env/bin/activate

pip3 install psycopg2
pip3 install django

code .
```

### Having trouble keeping up? If so, please use the following commands

```
git fetch --all
git checkout main
git reset --hard origin/main
```

The above commands will only function if you are in the `django-code-along` directory.

### Here are some helpful Django commands for this week (they are not listed in any particular order)

```
pip freeze > requirements.txt

django-admin startproject <mysite>
python3 manage.py startapp <myapp>

python3 manage.py createsuperuser

python3 manage.py runserver

python3 manage.py makemigrations
python3 manage.py migrate
```
