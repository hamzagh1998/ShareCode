# ShareCode

Full-featured website created with Django, the web development framework for Python.
<ul>
  <li>Register, update, authenticate, delete users</li>
  <li>Blog posting (Create, Retrieve, Update, Delete - CRUD)</li>
  <li>Building a comment/reply system</li>
  <li>Using filters<li>
</ul>

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

python3.6 or above

### Installing

To get the development env running

install all the packages inside the requirements.txt file
```
python -m pip install -r requirements.txt
```

## Running the tests

Make the migrations
```
python manage.py makemigrations
```

And migrate
```
python manage.py migrate
```

then create superuser
```
python manage.py createsuperuser
```

Finally run the server in your local machine
```
python manage.py runserver
```

## Authors

* **Hamza Ghenimi** - *Initial work* - [ShareCode](https://github.com/hamzagh1998/ShareCode.git)
