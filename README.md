# Requirements
* python version 3.5.1
* pip
* virtualenv
* mysql
  * username: `root`
  * password: `mysql`

# Install
```
git clone https://github.com/CISC475-Group2/parsons && cd parsons/
virtualenv venv -p python3.5
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

# Installation gotchas

* Our VM uses `tcsh` shell, so be sure to switch to `bash` or you will get errors doing the `source` command. Just type `bash` and you will log into the bash shell.

* Python 3.5.1 is required. Doesn't work with Python 3.4. Note that python 3.5 could be the `python3.5` command.
