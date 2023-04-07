# Posts Api Using Python and Graphql

## Configuration

```shell
pip install flask ariadne flask-sqlalchemy flask-cors psycopg2 python-dotenv
```

## Running

```shell
export FLASK_APP=app.py
```

then :
```shell
flask run
```

## Tips

* For this example, you can use a hosted SQL database like ElephantSQL, or you can use any SQL database you like.
* Ariadne is not compatible with graphql-core 3.1 so better to have Python <= 3.8 to avoid issues