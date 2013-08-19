#!/usr/bin/env python

import web
import hashlib

urls = (
	'/', 'index'
)

web.config.debug = True

def checkauth():
	mip = web.cookies(ipaddr=web.ctx.ip)
	mip.ipaddr

class index:
	def GET(self):
		return "hello world"

#if __name__ == "__main__":
app = web.application(urls, globals())
app.add_processor(web.loadhook(checkauth))
app.run()