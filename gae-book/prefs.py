from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import models

class PrefsPage( webapp.RequestHandler ):
	def post( self ):
		user = users.get_current_user()
		prefs = models.get_userprefs( user.user_id() )

		try:
			tz_offset = int( self.request.get('tz_offset') )
			prefs.tz_offset = tz_offset
			prefs.put()
		except:
			# user entered invalid info, ignore for now
			pass

		self.redirect( '/' )

application = webapp.WSGIApplication(
		[('/prefs', PrefsPage)],
		debug=True
	)

def main():
	run_wsgi_app( application )

if '__main__' == __name__:
	main()
