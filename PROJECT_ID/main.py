import webapp2
from PROJECT_NAME.Handlers.MainHandler import MainHandler
from PROJECT_NAME.Handlers.TokenHandler import TokenHandler
from PROJECT_NAME.Handlers.UserHandler import UserHandler
from PROJECT_NAME.Handlers.NotFoundHandler import NotFoundHandler

app = webapp2.WSGIApplication([
    
    # home
    webapp2.Route(r'', handler=MainHandler, name='MainHandler'),
    webapp2.Route(r'/', handler=MainHandler, name='MainHandler'),

	# token
    webapp2.Route(r'/token', handler=TokenHandler, name='TokenHandler'),
    webapp2.Route(r'/token/', handler=TokenHandler, name='TokenHandler'),
    webapp2.Route(r'/token/test', handler=TokenHandler, name='TokenHandler'),
    webapp2.Route(r'/token/test/', handler=TokenHandler, name='TokenHandler'),

    # user
    webapp2.Route(r'/user', handler=UserHandler, name='UserHandler'),
    webapp2.Route(r'/user/', handler=UserHandler, name='UserHandler'),  
    webapp2.Route(r'/user/<search:search>', handler=UserHandler, name='UserHandler'),
    webapp2.Route(r'/user/<search:search>/', handler=UserHandler, name='UserHandler'),  
    webapp2.Route(r'/user/<user_id:[a-zA-Z0-9]*>', handler=UserHandler, name='UserHandler'),  
    webapp2.Route(r'/user/<user_id:[a-zA-Z0-9]*>/', handler=UserHandler, name='UserHandler'),  
  
    
    # not found
    webapp2.Route(r'/<page:.*>', handler=NotFoundHandler, name='NotFoundHandler'),

], debug=True)

