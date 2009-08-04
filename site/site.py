import web, sys, markdown, gettext
gettext.install( "NONE" )
#sys.path.append( "./egbdf" )
#print sys.path
import egbdf.templates.index
import egbdf.templates.song

def _( s ):
	return "TRANSLATED('" + s + "')"

# so that sessions work, but can't hot-reload
#web.config.debug = False


urls = (
	'/', 'index',
#	'/dynamic/([a-z_-]+)', 'markdown',
	'/(.*[^/])/(.*[^/])/(.*[^/])', 'song',
)

def custom404():
	return web.notfound( _("Custom 404 Page Not Found") )

def custom500():
	return web.internalerror( _("Custom 500 Server Error") )

#class markdown:
#	def GET( self, filename ):
#		f = open( "./static/" + filename + ".txt" )
#		return markdown.markdown( "marked-down " + filename )

class song:
	def GET( self, instrument, composer, song ):
		web.header( "Content-Type", "text/html; charset=utf-8" )
		return egbdf.templates.song.song( instrument, composer, song )
		#return _("Hello World!") + "<br>INS: " + instrument + "<br>COMP: " + composer + "<br>SONG: " + song

class index:
	def GET( self ):
		web.header( "Content-Type", "text/html; charset=utf-8" )
		return egbdf.templates.index.index()

app = web.application( urls, globals() )
app.notfound = custom404
app.internalerror = custom500

if __name__ == "__main__":
	app.run()
