import json, webapp2, traceback, sys

from PROJECT_NAME.Models.BaseModel import *
from PROJECT_NAME.Models.Token import Token
from PROJECT_NAME.Models.User import User
from PROJECT_NAME.Errors import *


class BaseHandler(webapp2.RequestHandler):

	def __init__(self, request, response):
		db.create_tables([Token, User], safe=True)
		# self.PROJECT_NAME = PROJECT_NAME()

		response.headers["Content-Type"] = "application/json"	

		self.initialize(request, response)

	def get_params(self):
		try: 
			
			if self.request.body:
				return json.loads(self.request.body)
			else:
				params = self.request.params
				
				out = {}
				for key in params.keys():
					out[key] = params[key]

				return out

		except Exception as e:
			e.message = "Invalid Payload. Please check your JSON."
			raise e
			return None
		

	def assert_params(self, params, fields):
		for field in fields:
			if not params.get(field):
				e = BadRequestException()
				e.message = "Missing '%s' field" % (field)
				raise e
		

	def token(self):
		if "Authorization" in self.request.headers:
			return self.request.headers.get("Authorization")
		else:
			e = BadRequestException()
			e.message = "Missing Authorization Header"
			raise e

	def respond(self, a={}):
		
		try:
			db.close()
		except Exception as e:
			print e

		if self.response.body == "":
			self.response.write(json.dumps(a, separators=(',',':')))

	def error(self, e):

		print "\n=-=-=-=-=- ERROR -=-=-=-=-=\n"
		print traceback.format_exc()
		print " =-=-=-=-=-=-=-=-=-=-=-=-=-=\n"

		r = {}

		r["type"] = e.type if hasattr(e, "type") else e.__class__.__name__ 

		if hasattr(e, 'code'):
		   r["code"] = e.code
		else:
		   r["code"] = 500

		defaultMessage = ''.join(traceback.format_exception_only(type(e), e)).replace("\\", "").replace("\"", "").replace("\n", "")

		r["message"] = e.message or defaultMessage #"Something went wrong. Please contact jake@PROJECT_NAME.com."

		
		self.response.status = "%i %s" % (r["code"], r["type"])
		self.response.status_int = r["code"]
		self.response.status_message = r["message"]



		try:
			db.close()
		except Exception as e:
			print e
			print "DB already closed"

		self.response.write(json.dumps(r, separators=(',',':')))