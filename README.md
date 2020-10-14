# Demo
http://gaag.nom.za/

# Run
Copy dev.env to prod.env and fill environment variables.
Then: 
```
make run_prod
make django_prepare
```

# Tests
```bash
make run_dev
make tests
```

# API
## Get dishes example:
```
response = requests.get('http://gaag.nom.za/api', headers={'TOKEN': '123456'})
```

## Create dish example:
```python
dish_data = {
    'name': 'Мачуча',
    'price': 999,
    'nutritional_value': {
        'proteins': 0.1,
        'fats': 0.2,
        'carbohydrates': 0.3,
        'calories': 4000,
    },
    'category': 1,
}
response = requests.post('http://gaag.nom.za/api/', json=dish_data, headers={'TOKEN': '123456'})
```

# References
https://hub.docker.com/_/postgres

https://hub.docker.com/_/nginx

https://hub.docker.com/_/python

https://hub.docker.com/_/redis

https://www.django-rest-framework.org

https://www.djangoproject.com

https://docs.djangoproject.com/en/3.0/

https://django-model-utils.readthedocs.io/en/latest/index.html

https://docs.celeryproject.org/en/stable/index.html

https://pytest-django.readthedocs.io/en/latest/

https://www.postgresql.org/docs/13/index.html

https://vuejs.org

