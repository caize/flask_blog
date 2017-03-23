from api import photos,app
from flask import request,url_for,render_template
from api.func import md5
from api.views import admin_api, error, success
import datetime


@app.route('/up-img',methods=['POST'])
@admin_api
def upload():
  if request.method == "POST" and 'pic' in request.files:
    filename = photos.save(request.files['pic'],name=datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.')
    file_url = photos.url(filename)
    return success({"url":file_url})
  else:
    return error(500,'has some error')