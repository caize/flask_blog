from api import app
from api.models import Menu,MenuSchema
from flask import jsonify,request,abort
from api.views import before_api, error, success


@app.route('/menu')
@app.route('/menu/<int:id>')
@before_api
def menu(id=0):
  schema = MenuSchema(many=True)
  res = schema.dump(Menu.query.filter_by(pid=id).all())
  return success(res.data)