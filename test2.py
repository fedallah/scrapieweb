#!/usr/bin/env python

import web
import hashlib
import random
import time

urls = (
	'/', 'index'
)

app = web.application(urls, globals())

web.config.debug = True

def uniqidgen(ilist):
	sha512h = hashlib.new('sha512')
        "function accepts a list; generates a SHA512 hash based on input from list (64char hex output)"
	for i in ilist:
		sha512h.update(i)
	return sha512h.hexdigest()

def ckauth_proc():
	try:
		uid = web.cookies().get(userVal)
	except:
		keys = [ web.ctx.ip, time.clock(), random.random() ]
		uid = uniqidgen(keys)
		web.setcookie('userVal', uid, 3600)
	
class index:
	def GET(self):
		userid = web.cookies().get(userVal)
		if not userid:
			userid = "notfound"
		return "hello world" + userid

app.add_processor(web.loadhook(ckauth_proc))

if __name__ == "__main__":
	app.run()
