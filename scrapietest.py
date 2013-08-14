#!/usr/bin/env python

import web
import time
import hashlib

sha2 = hashlib.sha256()

db = web.database(dbn='postgres', db='scrapieweb', user='postgres', pw='fuddruckers')

# def uservalidate(username):
#	usernum = db.query("SELECT COUNT(*) FROM auth WHERE username=$uid", vars="username")	
#	return usernum[0]
	
def cookievalidate(ck):
	try:
		return web.cookies().ck
	except:
		return 0
	
urls = (
	'/(.*)', 'index'
	'/checkauth', 'CheckAuth'
)

passval = web.form.regexp(r".{25,60}", 'must be between 25 and 60 characters')

# login_form = web.form.Form(
#	web.form.Textbox("username", description="Username"),
#	web.form.Password("password", passval, description="Password"),
#	web.form.Button("submit", type="submit", description="Login"),
#	validators = [
#		web.form.Validator("User already exists; please select a different username.", uservalidate("username") == 0)
#	]
#)

app = web.application(urls, globals())

web.config.debug = True

if __name__ == "__main__":
    app.run()

class CheckAuth:
	def GET(self):
		try:
			thism = web.cookies().isauth
		except:
			return "not authorized"
		else:
			try:
				thismdb = db.select('auth', what="expire,isauth,secsvalid", vars=thism, where="isauth = $isauth", _test=True)
			except:
				return "not authorized"
			else:
				if thismdb[1]:
					db.delete('auth', where='isauth = $isauth', vars=thism, _test=True)
					return "not authorized"
				elif thismdb[0].expire < time.time():
					return "not authorized"
				else:
					return "authorized"
class index:
	def GET(self):
		return "hello world"
