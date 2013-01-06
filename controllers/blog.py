import web
from configs import settings

db = settings.db
render = settings.render

class Index:
	def GET(self):
		return 'index page'

class View:
	def GET(self,id):
		return 'view page'+id

class New:
	def GET(self):
		return 'new page'

class Edit:
	def GET(self,id):
		return 'edit page'+id

class Delete:
	def GET(self,id):
		return 'delete page'+id

