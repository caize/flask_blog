from api import app
from api.models import Menu,MenuSchema
from flask import jsonify,request,abort
from api.views import admin_api, error, success


@app.route('/admin/menu')
@admin_api
def admin_menu():
  schema = MenuSchema(many=True)
  res = schema.dump(Menu.query.filter_by(pid=0).all())
  r_menu = res.data
  for s in r_menu:
    sub = schema.dump(Menu.query.filter_by(pid=s['id']).all())
    s['sub'] = sub.data
  return success(r_menu)

@app.route('/admin/menu/<int:id>')
@admin_api
def show_one_menu(id):
  schema = MenuSchema()
  res = schema.dump(Menu.query.filter_by(id=id).first())
  return success(res.data)