#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import wsgiref.handlers
import os
import facebook

from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util

class BaseHandler( webapp.RequestHandler ):
    def get( self ):
        self.API_KEY = '0eda365a1ca6aa048b65467aae47e520'
        self.SECRET_KEY = 'eccef02b91732d24f7cdf37dfded3751'
        self.facebookapi = facebook.Facebook( self.API_KEY, self.SECRET_KEY )

        if not self.facebookapi.check_connect_session( self.request ):
            self.tpl( 'login.html' )
            return

        try:
            self.user = self.facebookapi.users.getInfo(
              [ self.facebookapi.uid ],
              [ 'uid', 'name', 'birthday' ][0]
            )
        except facebook.FacebookError:
            self.tpl( 'login.html' )
            return

        self.get_secure()

    def tpl( self, tpl_file, vars = {} ):
        vars['apikey'] = self.API_KEY
        path = os.path.join( os.path.dirname( __file __ ), 'templates/' + tpl_file )
        self.response.out.write( template.render( path, vars ) )

class MainHandler( BaseHandler ):
#    def get(self):
#        self.response.out.write('Hello world!')

    def get_secure( self ):
        template_values = {
            'uid': self.user['uid'],
            'name': self.user['name'],
            'birthday': self.user['birthday'],
        }

        self.tpl( 'index.html', template_values )

def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
