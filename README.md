# Requirements
* python version 3.5.1

* pip

* virtualenv

# Install
```
sudo pip install virtualenv
git clone https://github.com/CISC475-Group2/Parsons && cd Parsons/
virtualenv venv -p `which python3`
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

To create an admin user:

```
python manage.py createsuperuser
```
