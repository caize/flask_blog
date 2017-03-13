from . import app
from .func import md5
from .models import Oauth
from flask import jsonify,request,abort,make_response
from . import cache
import time,functools,six
from datetime import timedelta


def error(code, msg):
  return make_response(jsonify({"error":msg}), code)

def success(data):
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


@app.route('/')
def index():
  return jsonify({"token":"dadsas"})


@app.route('/token',methods = ['POST'])
def createToken():
  if request.json is None:
    abort(500,'appid or secret is none')
  appid = request.json.get('appid')
  secret = request.json.get('secret')
  ip = request.remote_addr
  if appid is None or secret is None:
    abort(500,'appid or secret is none')
  else:
    oath = Oauth.query.filter_by(appid = appid,secret = secret).first()
    if oath is None:
      abort(500,'Invalid appid & secret')
    else:
      if cache.get(appid) is None:
        token = md5("%s%s%s%s"%(ip,appid,secret,time.time()))
        cache.set(appid,token,timeout=1800)
        cache.set(token,appid,timeout=1800)
      else:
        token = cache.get(appid)
    return jsonify({"token":token})