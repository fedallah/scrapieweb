#!/usr/bin/env python

import web
import hashlib

urls = (
	'/', 'index'
)

web.config.debug = True

def checkauth():
	
app.add_processor(web.loadhook(checkauth))

class index:
	def GET(self):
		return "hello world"

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
