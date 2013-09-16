#!/usr/bin/env python

import web
import hashlib
import json
import random
import time
import re

rval = 0

# handle connection to control database.  if it doesn't exist this thing
# will not start.
def controlconnect():
	try:
		controldb = web.database(dbn='sqlite', db='/fsart/cdb.sqlite3')
	except:
		return 1
	else:
		return 0

global gmrval = controlconnect()
		
urls = (
	'/', 'status',
	'/config', 'config',
	'/err', 'error'
	'/mdbupdate', 'master_db_update',
	'/nt', 'newtarget',
	'/nm', 'newmaster',
	'/jobadd', 'job_add',
	'/jobcancel', 'job_cancel',
)

web.config.debug = True

app = web.application(urls, globals())

# this problem-checking code will run every time a request is made.
# is the control db [still] available?  do we have a master configured?
def hasmaster():
	if gmrval == 1:
		rval = controlconnect()
	else:	
		try:
			masters = controldb.query("SELECT COUNT FROM masters")
			if masters < 1:
				rval = 3
		except:
			rval = 1
	if rval > 0:
		global gmrval = rval
		# show the error page if there is one
		raise web.seeother('/err')
	else:
		global gmrval = 0
		
def ishuman():
	mq = web.ctx.query
	if "human" in mq.lower():
		web.header('Content-type', "text/html; charset=utf-8")
	else:
		web.header('Content-type', "application/json; charset=utf-8")
		
def islocked():
	if gmrval == 1:
		rval = controlconnect()
	else:
		try:
			queued = controldb.query("SELECT COUNT FROM jobs")
		except:
			rval = 1
	if rval > 0:
		global gmrval = rval
		raise web.seeother('/err')
	else:
		global gmrval = 0				
	

# what is the status of the worker?  is it busy?  what is it doing?
class status:
	

class error:
	def GET(self):
		mq = web.ctx.query
		if "human" in mq.lower():
	
	else:
		return gmrval
	
class job_cancel:

class 
	
app.add_processor(web.loadhook(hasmaster))
app.add_processor(ishuman)
	
if __name__ == "__main__":
	app.run()
