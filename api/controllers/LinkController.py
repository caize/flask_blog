from api import app,db
from api.models import Link,LinkSchema,Tag,TagSchema,Daily,DailySchema,PostsSchema,Posts,MenuSchema,Menu
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
  start_id = request.args.get('start_id')
  last_id = ''
  schema = DailySchema(many=True)
  one_schema = DailySchema()
  if start_id is None:
    res = schema.dump(Daily.query.order_by('date desc').limit(12).all())
  else:
    res = schema.dump(Daily.query.filter(Daily.id <= int(start_id)).order_by('date desc').limit(12).all())
  ret = res.data
  if len(ret) > 0:
    lastInfo = one_schema.dump(Daily.query.filter(Daily.id < ret[len(ret) - 1]['id']).order_by('date desc').first()).data
    if lastInfo is not None and len(lastInfo) > 0:
      last_id = lastInfo['id']
  return success({'lists':ret,'last_id':last_id})

@app.route('/posts/<int:id>')
@app.route('/posts')
@before_api
def get_posts(id=None):
  top = request.args.get('top')
  start_id = request.args.get('start_id')
  if id is not None:
    schema = PostsSchema()
    menu_schema = MenuSchema()
    tag_schema = TagSchema(many=True)
    p = Posts.query.get(id)
    ret = schema.dump(p)
    info = ret.data
    if info is not None and len(info) > 0:
      info['menu'] = menu_schema.dump(Menu.query.get(info['menu_id'])).data
      info['next'] = schema.dump(Posts.query.filter(Posts.id > id).first()).data
      info['prev'] = schema.dump(Posts.query.filter(Posts.id < id).order_by('id desc').first()).data
      info['tagList'] = tag_schema.dump(Tag.query.filter(Tag.id.in_(info['tags'].split(','))).all()).data
    p.click_num = p.click_num + 1
    db.session.commit()
    return success(info)
  elif top is None:
      menu_id = request.args.get('menu_id')
      if menu_id is None:
        schema = PostsSchema(many=True)
        one_schema = PostsSchema()
        menu_schema = MenuSchema()
        tag_schema = TagSchema(many=True)
        if start_id is not None:
          lists = schema.dump(Posts.query.filter(Posts.id <= int(start_id)).order_by('push_at desc').limit(9).all()).data
        else:
          lists = schema.dump(Posts.query.order_by('push_at desc').limit(9).all()).data
        last_id = 0
        for i in lists:
          i['menu'] = menu_schema.dump(Menu.query.get(i['menu_id'])).data
          i['tagList'] = tag_schema.dump(Tag.query.filter(Tag.id.in_(i['tags'].split(','))).all()).data
        if len(lists) > 0:
          lastInfo = one_schema.dump(Posts.query.filter(Posts.id < lists[len(lists) - 1]['id']).order_by('push_at desc').first()).data
          if lastInfo is not None and len(lastInfo) > 0:
            last_id = lastInfo['id']
        ret = {'lists':lists, 'last_id': last_id}
        return success(ret)
      else:
        schema = PostsSchema(many=True)
        one_schema = PostsSchema()
        menu_schema = MenuSchema()
        tag_schema = TagSchema(many=True)

        some_menu_schema = MenuSchema(many=True)
        menus = some_menu_schema.dump(Menu.query.filter(Menu.pid==menu_id)).data
        menuids = [menu_id]
        for m in menus:
          menuids.append(m['id'])

        if start_id is not None:
          lists = schema.dump(Posts.query.filter(Posts.menu_id.in_(menuids)).filter(Posts.id <= int(start_id)).order_by('push_at desc').limit(9).all()).data
        else:
          lists = schema.dump(Posts.query.filter(Posts.menu_id.in_(menuids)).order_by('push_at desc').limit(9).all()).data
        last_id = 0
        for i in lists:
          i['menu'] = menu_schema.dump(Menu.query.get(i['menu_id'])).data
          i['tagList'] = tag_schema.dump(Tag.query.filter(Tag.id.in_(i['tags'].split(','))).all()).data
        if len(lists) > 0:
          lastInfo = one_schema.dump(Posts.query.filter(Posts.id < lists[len(lists) - 1]['id']).order_by('push_at desc').first()).data
          if lastInfo is not None and len(lastInfo) > 0:
            last_id = lastInfo['id']
        ret = {'lists':lists, 'last_id': last_id}
        return success(ret)
  else:
    if top is not None:
      schema = PostsSchema(many=True)
      menu_schema = MenuSchema()
      tag_schema = TagSchema(many=True)
      alists = schema.dump(Posts.query.order_by('click_num desc').limit(top).all()).data
      for info in alists:
        if info is not None and len(info) > 0:
          info['menu'] = menu_schema.dump(Menu.query.get(info['menu_id'])).data
          info['tagList'] = tag_schema.dump(Tag.query.filter(Tag.id.in_(info['tags'].split(','))).all()).data
      return success(alists)