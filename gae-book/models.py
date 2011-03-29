from google.appengine.api import memcache
from google.appengine.api import users
from google.appengine.ext import db

class UserPrefs( db.Model ):
	tz_offset = db.IntegerProperty( default=0 )
	user = db.UserProperty( auto_current_user_add=True )

	def put_cache( self ):
		"""Put the current object into the given memcache namespace."""
		memcache.set( self.key().name(), self, namespace="UserPrefs" )

	@staticmethod
	def get_cache( user_id ):
		"""Static method to look for the given user_id in memcache."""
		prefs = memcache.get( user_id, "UserPrefs" )
		return prefs

	def put( self ):
		"""Update the cache, then continue datastore put."""
		self.put_cache()
		db.Model.put( self )

def get_userprefs( user_id ):
	"""Return user preferences for the given user_id (usually from user.get_current_user().user_id())"""
	key = db.Key.from_path( 'UserPrefs', user_id )

	prefs = UserPrefs.get_cache( user_id )
	if not prefs:
		prefs = db.get( key )  # datastore preferences

		if prefs:
			prefs.put_cache()
		else:
			prefs = UserPrefs( key_name=user_id )  # default preferences (unconfigured)

	return prefs
	

