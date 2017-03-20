from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow  import Marshmallow
from flask_cors import CORS,cross_origin
from flask_cache  import Cache
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import pymysql,os

app = Flask(__name__, instance_relative_config=True)
# app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()+'/static'
app.config['UPLOADED_PHOTO_DEST'] = './static'
app.config['UPLOADED_PHOTO_ALLOW'] = IMAGES

photos = UploadSet('PHOTO')
configure_uploads(app, photos)
# patch_request_class(app)

app.config.from_object('config')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
ma = Marshmallow(app)
cache = Cache(app)
cache.init_app(app)
CORS(app)
admin_pass = '667bfb2d66fa79699ee2ace21d1863af'

from api import models,views,controllers
