from flask.views import MethodView
from api import app,db
from api.models import Menu,MenuSchema,LinkSchema,Link,Tag, TagSchema
from flask import jsonify,request,abort
from api.views import admin_api, error, success
from sqlalchemy import or_
import datetime

#menu of admin
class MenuAPI(MethodView):
  decorators = [admin_api]

  def get(self, id):
    if id is None:
      schema = MenuSchema(many=True)
      res = schema.dump(Menu.query.filter_by(pid=0).all())     
      r_menu = res.data
      for s in r_menu:
        sub = schema.dump(Menu.query.filter_by(pid=s['id']).all())
        s['sub'] = sub.data
      return success(r_menu)
    else:
      schema = MenuSchema()
      res = schema.dump(Menu.query.filter_by(id=id).first())
      return success(res.data)

  def post(self):
    name = request.json.get('name')
    pid = request.json.get('pid')
    schema = MenuSchema()
    res = schema.dump(Menu.query.filter_by(name=name).first())
    if res.data is None or len(res.data) == 0:
      db.session.add(Menu(name, pid))
      db.session.commit()
    return success()
  # 1.find submenu of this menu , if is not none , return error
  def delete(self, id):
    schema = MenuSchema()
    sub_menu = schema.dump(Menu.query.filter_by(pid=id).first())
    if sub_menu.data is None  or len(sub_menu.data) == 0:
      Menu.query.filter(Menu.id==id).delete()
      db.session.commit()
      return success()
    else:
      return error(500,'has some submenu of this menu, cat not delete!')

  def put(self, id):
    schema = MenuSchema()
    name = request.json.get('name')
    pid = request.json.get('pid')
    m = schema.dump(Menu.query.filter(Menu.name==name).filter(Menu.id!=id).first())
    if m.data is None or len(m.data) == 0:
      n = Menu.query.filter(Menu.id==id).first()
      n.name = name
      n.pid = pid
      db.session.commit()
    return success()

#link fo admin
class LinkAPI(MethodView):
  decorators = [admin_api]

  def get(self, id):
    if id is None:
      schema = LinkSchema(many=True)
      res = schema.dump(Link.query.all())
      return success(res.data)
    else:
      schema = LinkSchema()
      res = schema.dump(Link.query.filter_by(id=id).first())
      return success(res.data)

  def post(self):
    title = request.json.get('title')
    desc = request.json.get('desc')
    url = request.json.get('url')
    schema = LinkSchema()
    has = schema.dump(Link.query.filter(or_(Link.title == title,Link.url == url)).first())
    if has.data is None or len(has.data) == 0:
      db.session.add(Link(title=title, url=url, desc=desc))
      db.session.commit()
    return success()

  def put(self, id):
    title = request.json.get('title')
    desc = request.json.get('desc')
    url = request.json.get('url')
    schema = LinkSchema()
    has = schema.dump(Link.query.filter(or_(Link.title == title,Link.url == url)).filter(Link.id!=id).first())
    if has.data is None or len(has.data) == 0:
      n = Link.query.get(id)
      n.title = title
      n.url = url
      n.desc = desc
      db.session.commit()
    return success()

  def delete(self, id):
    link = Link.query.get(id)
    db.session.delete(link)
    db.session.commit()
    return success()


#tag 
class TagAPI(MethodView):
  decorators = [admin_api]

  def get(self, id):
    search = request.args.get('search')
    schema = TagSchema(many=True)
    if search is not None:
      res = schema.dump(Tag.query.filter(Tag.name.like("%" + search + "%")).all())
      return success(res.data)
    else:
      res = schema.dump(Tag.query.order_by(desc(Tag.add_at)).all())
      return success(res.data)

  def post(self):
    name = request.json.get('name')
    schema = TagSchema()
    if name is not None:
      res = schema.dump(Tag.query.filter_by(name=name).first())
      if res.data is None or len(res.data) == 0:
        db.session.add(Tag(name=name,add_at=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        db.session.commit()
    return success()

  def put(self, id):
    pass

  def delete(self, id):
    pass