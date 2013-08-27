#!/usr/bin/env python

import web
import hashlib
import random
import time

rval = 0

try:
	controldb = web.database(dbn='sqlite', db='/etc/fsart/control')
except:
	rval = 1	

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

def hasmaster():
	if rval = 0:
		try:
			masters = controldb.query("SELECT COUNT FROM masters")
			if masters > 1:
				rval = 2
		except:
			rval = 1
	if rval > 0:
		global gmrval = rval
		raise web.seeother('/err')
	else:
		global gmrval = None
	
def getstatus():
	
class status:

class error:
	if web.ctx.query = human:
	
	else:
		return gmrval
	
class job_cancel:
	
app.add_processor(web.loadhook(getstatus))
	
if __name__ == "__main__":
	app.run()