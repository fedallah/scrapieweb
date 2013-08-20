#!/usr/bin/env python

import web
import hashlib
import time

mkhash = hashlib.sha512

app = web.application(urls, globals())

urls = (
	'/', 'index'
)

web.config.debug = True

def checkauth(cahandle):
	mkhash.update(web.ctx.ip + time.clock() + random.random())
	uniqid = mkhash.hexdigest()
	

class index:
	def GET(self):
		return "hello world"

class noauth:
	def GET(self):
		return "not authorized"

app.add_processor(web.loadhook(checkauth))

if __name__ == "__main__":
	app.run()
