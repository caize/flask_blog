from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow  import Marshmallow
from flask_cors import CORS,cross_origin
from flask_cache  import Cache
import pymysql

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
ma = Marshmallow(app)
cache = Cache(app)
cache.init_app(app)
CORS(app)

from api import models,views,controllers
