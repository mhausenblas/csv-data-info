import logging, cgi, os, platform, sys, urllib, time

from google.appengine.ext import webapp
from google.appengine.api import memcache
from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp import template


class APIHandler(webapp.RequestHandler):
	def get(self):
		logging.debug('[API] call:"%s" from IP:%s' %(self.request.query_string, os.environ['REMOTE_ADDR']))
		#self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.out.write('API available')