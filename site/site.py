import web, sys, markdown, gettext
gettext.install( "NONE" )

#def _( s ):
#	return "TRANSLATED('" + s + "')"

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
		host = web.ctx.env['HTTP_HOST']
		lang = host.split('.')[0]
		render = web.template.render( 'egbdf/templates', globals={'_': _} )
		return render.song( lang=lang, instrument=instrument, composer=composer, song=song )

class index:
	def GET( self ):
		web.header( "Content-Type", "text/html; charset=utf-8" )
		host = web.ctx.env['HTTP_HOST']
		lang = host.split('.')[0]
		render = web.template.render( 'egbdf/templates', globals={'_': _} )
		return render.index( lang=lang )

app = web.application( urls, globals() )
app.notfound = custom404
app.internalerror = custom500

if __name__ == "__main__":
	app.run()
