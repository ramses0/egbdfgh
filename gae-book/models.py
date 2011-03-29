from google.appengine.api import users
from google.appengine.ext import db

class UserPrefs( db.Model ):
	tz_offset = db.IntegerProperty( default=0 )
	user = db.UserProperty( auto_current_user_add=True )

def get_userprefs( user_id ):
	"""Return user preferences for the given user_id (usually from user.get_current_user().user_id())"""
	key = db.Key.from_path( 'UserPrefs', user_id )
	prefs = db.get( key )
	if not prefs:
		prefs = UserPrefs( key_name=user_id )
	return prefs
	

