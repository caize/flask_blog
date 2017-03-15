from api import app,db
from api.models import Link,LinkSchema,Tag,TagSchema,Daily,DailySchema
from flask import jsonify,request,abort
from api.views import before_api, error, success
from flask_cors import CORS,cross_origin
import datetime


@app.route('/link')
@cross_origin()
@before_api
def link():
  schema = LinkSchema(many=True)
  res = schema.dump(Link.query.all())
  return success(res.data)

@app.route('/tag')
@cross_origin()
@before_api
def tag():
  schema = TagSchema(many=True)
  res = schema.dump(Tag.query.order_by('add_at desc').all())
  return success(res.data)

@app.route('/daily')
@cross_origin()
@before_api
def addTag():
  schema = DailySchema(many=True)
  res = schema.dump(Daily.query.order_by('date desc').all())
  return success(res.data)