import web

db = web.database(dbn='mysql', db='blogs', user='root', pw='admin')

t_globals = {
	'site_name':'my own blogs'
}

render = web.template.render('templates', base='base', globals=t_globals)



