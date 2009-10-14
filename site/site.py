import web, sys, markdown, gettext
gettext.install( "NONE", "" )

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

class page:
	def GET( self ):
		print "ABCDEFG"
		self.globals = {
				'_': _
		}
		web.header( "Content-Type", "text/html; charset=utf-8" )
		host = web.ctx.env['HTTP_HOST']
		self.lang = host.split('.')[0]
		

class song( page ):
	def GET( self, instrument, composer, song ):
		# super
		page.GET( self )
		render = web.template.render( 'egbdf/templates', self.globals )
		return render.song( lang=self.lang, instrument=instrument, composer=composer, song=song )

class index( page ):
	def abc( self, a):
		return "abc"
	def GET( self ):
		# super
		page.GET( self )
		print self.globals
		print self.lang
		render = web.template.render( 'egbdf/templates', globals=self.globals )
		return render.index( lang=self.lang )

app = web.application( urls, globals() )
app.notfound = custom404
app.internalerror = custom500

if __name__ == "__main__":
	app.run()
