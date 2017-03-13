from . import db,ma
class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
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
    title = db.Column(db.String(40))
    desc = db.Column(db.String(100))
    img = db.Column(db.String(200), default=None)
    url = db.Column(db.String(100))

class LinkSchema(ma.Schema):
    class Meta:
        fields = ('id','title','desc','img','url')