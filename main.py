"""
The main GAE script.

@author: Michael Hausenblas, http://sw-app.org/mic.xhtml#i
@since: 2011-04-17
@status: inital version
"""
import logging, cgi, os, platform, sys

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from handler import *


application = webapp.WSGIApplication([
						('/api/', APIHandler)
					],
					debug=False)

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
	main()
