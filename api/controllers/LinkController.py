from api import app
from api.models import Link,LinkSchema
from flask import jsonify,request,abort
from api.views import before_api, error, success


@app.route('/link')
@before_api
def link():
  schema = LinkSchema(many=True)
  res = schema.dump(Link.query.all())
  return success(res.data)