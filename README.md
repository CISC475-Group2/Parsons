# Requirements
* python version 3.5.1 (important)
* pip
* virtualenv
* mysql
  * username: `root`
  * password: `mysql`

# Install
```
git clone https://github.com/CISC475-Group2/parsons && cd parsons/
virtualenv venv -p python3.5
bash
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata initial_data
python manage.py runserver
```

Note - on the VM use
```
python manage.py runserver 0.0.0.0:8000
```

To create an admin user:

```
python manage.py createsuperuser
```

There is a test user with these credentials:
* username: `johnsmith`
* password: `password123`

# Working on the project
Make sure you have the `(venv)` sign in your terminal. If you don't, do `source venv/bin/activate` in terminal. Our VM uses `tcsh` shell, so be sure to switch to `bash` or you will get errors doing the `source` command. Just type `bash` and you will log into the bash shell.

# Testing

Right now we have two tests

`python manage.py test app`

`python manage.py test racketparser`
