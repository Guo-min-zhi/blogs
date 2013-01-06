import web
from configs import settings
from datetime import datetime

db = settings.db
render = settings.render

class Index:
	def GET(self):
		blogs = db.select('blogs', order = 'create_time desc')
		return render.index(blogs) 

class View:
	def GET(self,id):
		return 'view page'+id

class New:
	def GET(self):
		return render.new('aa')
	def POST(self):
		i = web.input()
		title = i.get('title', None)
		content = i.get('content', None)
		db.insert('blogs', title = title, content = content, create_time = datetime.now())
		raise web.seeother('/')


class Edit:
	def GET(self,id):
		return 'edit page'+id

class Delete:
	def GET(self,id):
		return 'delete page'+id

