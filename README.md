# Visualize importance of using Django QuerySets wisely

* Clone the repo
```
git clone git@github.com:gvkunchev/django_queryset_benchmark.git
```
* Create virtualenv
```
python -m venv venv
```
* Activate the virtualenv
```
.\venv\Scripts\activate
```
* Install requirements
```
python -m pip install -r requirements.txt
```
* Run migrations
```
python manage.py migrate
```
* Populate with fake data (takes a while)
```
python manage.py seed example --number=1000
```
* Run the server
```
python manage.py runserver
```
* See the results
```
http://localhost:8000
```

