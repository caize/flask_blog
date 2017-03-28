# -*- coding: utf-8 -*-
from . import app,db
from .func import md5
from .models import Oauth,Token,TokenSchema
from . import admin_pass
from flask import jsonify,request,abort,make_response,render_template
from . import cache
import time,functools,six
from datetime import timedelta


def error(code, msg):
  return make_response(jsonify({"error":msg}), code)

def success(data = []):
  return make_response(jsonify({"error":'',"data":data}), 200)

#token 验证
def before_api(fn):
  @functools.wraps(fn)
  def wrapper(*args, **kw):
    appid = request.headers.get('appid')
    secret = request.headers.get('secret')
    if appid is None or secret is None:
      return error(401,"appid or secret is none")
    else:
      oath = Oauth.query.filter_by(appid = appid,secret = secret).first()
      if oath is None:
        return error(401,"Invalid appid & secret")
    return fn(*args, **kw)
  return wrapper

def admin_api(fn):
  @functools.wraps(fn)
  def wrapper(*args, **kw):
    appid = request.headers.get('appid')
    secret = request.headers.get('secret')
    token = request.headers.get('token')
    if appid is None or secret is None:
      return error(401,"appid or secret is none")
    else:
      oath = Oauth.query.filter_by(appid = appid,secret = secret).first()
      if oath is None:
        return error(401,"Invalid appid & secret")
      else:
        if token is None:
          return error(401,'this token is not matching the appid')
        else:
          t = Token.query.filter_by(token=token).first()
          if t is not None:
            if float(t.time) < time.time():
              return error(401,"Invalid token")
          else:
            return error(401,"Invalid token")
    return fn(*args, **kw)
  return wrapper

@app.route('/')
def index():
  return jsonify({"token":"dadsas"})


@app.route('/token',methods = ['POST'])
def createToken():
  if request.json is None:
    return error(500,'appid or secret is none')
  appid = request.headers.get('appid')
  secret = request.headers.get('secret')
  ip = request.remote_addr
  password = request.json.get('password')
  if md5(password) != admin_pass:
    return error(500,'password is error')
  if appid is None or secret is None:
    return error(500,'appid or secret is none')
  else:
    oath = Oauth.query.filter_by(appid = appid,secret = secret).first()
    if oath is None:
      return error(500,'Invalid appid & secret')
    else:
      t = Token.query.first()
      if t is not None:
        if float(t.time) < time.time():
          token = md5("%s%s%s%s"%(ip,appid,secret,time.time()))
          t.token = token
          t.time = time.time() + 3600
          db.session.commit()
        else:
          token = md5("%s%s%s%s"%(ip,appid,secret,time.time()))
          t.token = token
          t.time = time.time() + 3600
          db.session.commit()
      else:
        token = md5("%s%s%s%s"%(ip,appid,secret,time.time()))
        db.session.add(Token(token=token,time=time.time() + 3600))
        db.session.commit()
    return success({"token":token})