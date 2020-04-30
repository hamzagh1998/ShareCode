# Project Title

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
python -m requirements.txt
```

## Running the tests

First create media folder inside the src folder

Make the migrations
```
python manage.py makemigrations
```

And migrate
```
python manage.py migrate
```

Collect the staticfiles
```
python manage.py collectstatic
```

And create superuser
```
python manage.py createsuperuser
```

Finally run the server in your local machine
```
python manage.py runserver
```

## Authors

* **Hamza Ghenimi** - *Initial work* - [PurpleBooth](https://github.com/hamzagh1998/ShareCode.git)
