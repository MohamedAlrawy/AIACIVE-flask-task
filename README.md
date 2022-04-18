# AIACIVE-flask-task
Flask users app for AIACTIVE company (Hiring process.)

### Create virtual environment, activate and install requirements
```pip install virtualenv```

```virtualenv .venv```

```source .venv/bin/activate```

```pip install -r requirements/requirements.txt```


### Run app
```python models.py```

```export FLASK_ENV=development```

```set FLASK_ENV=development```

```flask run```


To try APIs you can postman and kindly follow these steps:

- For listing users request on `localhost:5000/users/`.
- For adding new user request on `localhost:5000/users/`. The request body should be like:

```
{
    'name': 'string',
    'email': 'string@string.string'
}
```
- For retrieving specific user request on `localhost:5000/users/<int:id>/`.
- - For updating specific user request on `localhost:5000/users/<int:id>/`. The request body should be like:

```
{
    'name': 'string',
    'email': 'string@string.string'
}
```
- For deleting specific user request on `localhost:5000/users/<int:id>/`.
