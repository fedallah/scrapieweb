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
		sha512h.update(str(i))
	return sha512h.hexdigest()

def ckauth_proc():
	uid = web.cookies().get('userVal')
	if not uid:
		keys = [ web.ctx.ip, time.clock(), random.random() ]
		uid = uniqidgen(keys)
		web.setcookie('userVal', uid, 7200)
	
class index:
	def GET(self):
		userid = web.cookies().get('userVal')
		return "hello, " + userid

class target:
	def __init__(self):
	def verify:
	def scrape:
	def remove:
	
class file:
	def __init__(self):
	def verify:
	def update:

class filetype:
	def add:
	def remove:
		
class fetchall_page:
	def GET(self):
	

app.add_processor(web.loadhook(ckauth_proc))

if __name__ == "__main__":
	app.run()
