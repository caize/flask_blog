from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow  import Marshmallow
from flask_cors import CORS,cross_origin
from flask_cache  import Cache
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import pymysql,os


app = Flask(__name__, instance_relative_config=True,static_url_path='/static')
app.config['UPLOADED_PHOTO_DEST'] = os.getcwd()+'/api/static'
app.config['UPLOADED_PHOTO_ALLOW'] = IMAGES
app.config['UPLOADED_PHOTO_URL'] = 'http://localhost:5000/static/'

photos = UploadSet('PHOTO')
configure_uploads(app, photos)
patch_request_class(app)

app.config.from_object('config')
app.config.from_pyfile('config.py')


db = SQLAlchemy(app)
ma = Marshmallow(app)
cache = Cache(app)
cache.init_app(app)
CORS(app)
admin_pass = 'your admin pass md5'

from api import models,views,controllers
