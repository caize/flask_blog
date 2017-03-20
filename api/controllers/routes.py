from .Controller import MenuAPI,LinkAPI,TagAPI
from api import app

def add_api(api_name, api_class, url, pk='id', pk_type='int'):
  view = api_class.as_view(api_name)
  app.add_url_rule(url, defaults={'id': None},view_func=view, methods=['GET',])
  app.add_url_rule(url, view_func=view, methods=['POST',])
  app.add_url_rule('%s/<%s:%s>' % (url, pk_type, pk), view_func=view, methods=['GET', 'PUT', 'DELETE'])

add_api('admin_menu', MenuAPI, '/admin/menu')

add_api('admin_link', LinkAPI, '/admin/link')

add_api('admin_tag', TagAPI, '/admin/tag')