#!/usr/bin/env python

import web

urls = (
	'/', 'index'
)

app = web.application(urls, globals())

class index:
	def GET(self, name):
		if not name:
			name = 'World'
		return 'Hello, ' + name

if __name__ = "__main__":
	app.run()
