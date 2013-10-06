#!/usr/bin/env python3

import web
import hashlib
import random
import time
import re

urls = (
	'/', 'status',
	'/admin', 'admin'
	'/err', 'error'
)

class status:
	