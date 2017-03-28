# -*- coding: utf-8 -*-
from . import db,ma
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import func
import datetime

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    desc = db.Column(db.Text)
    content = db.Column(db.Text)
    push_at = db.Column(db.String(50))
    click_num = db.Column(db.Integer,default=10)
    menu_id = db.Column(db.Integer)
    tags = db.Column(db.String(100))
    img_url = db.Column(db.String(100))

class PostsSchema(ma.Schema):
    class Meta:
        fields = ('id','title','desc','content','push_at','click_num','menu_id','tags', 'img_url')


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    pid = db.Column(db.Integer, default=0)
    def __init__(self, name, pid):
        self.name = name
        self.pid = pid

    def __repr__(self):
        return '<User %r>' % self.name

class MenuSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'pid')

class Oauth(db.Model):
    appid = db.Column(db.String(20), primary_key=True)
    secret = db.Column(db.String(100))

class OauthSchema(ma.Schema):
    class Meta:
        fields = ('appid','secret')

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), unique=True)
    desc = db.Column(db.String(100))
    img = db.Column(db.String(200), default=None)
    url = db.Column(db.String(100), unique=True)

class LinkSchema(ma.Schema):
    class Meta:
        fields = ('id','title','desc','img','url')

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    add_at = db.Column(TIMESTAMP, server_default=func.now())
    def __init__(self, name, add_at):
        self.name = name
        self.add_at = add_at

class TagSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'add_at')

class Daily(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, server_default=func.now())
    text = db.Column(db.Text)

class DailySchema(ma.Schema):
    class Meta:
        fields = ('id','date','text')

class Token(db.Model):
    __tablename__ = 'token'
    token = db.Column(db.String(100),primary_key=True)
    time = db.Column(db.String(40))
    def __init__(self, token, time):
        self.token = token
        self.time = time

class TokenSchema(ma.Schema):
    class Meta:
        fields = ('token','time')