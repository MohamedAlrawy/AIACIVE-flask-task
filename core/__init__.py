from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

base_dir = os.getcwd()
app = Flask(__name__)

# config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{base_dir}/aiactive.db"

# connect to database
models = SQLAlchemy(app)
serializer = Marshmallow(app)


# import and register Blueprints
from .users import users
app.register_blueprint(users, url_prefix='/users')
