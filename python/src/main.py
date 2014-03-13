#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import webapp2

from core import admin_mod
from core import front_mod

from core import config

app = webapp2.WSGIApplication([
    webapp2.Route('/' + config.get_config('admin') + '/',                                               handler= admin_mod.load),
    webapp2.Route('/' + config.get_config('admin') + '/<module:/>',                                     handler= admin_mod.load),
    webapp2.Route('/' + config.get_config('admin') + '/<module:/[\w]+>',                                handler= admin_mod.load),
    webapp2.Route('/' + config.get_config('admin') + '/<module:/>/<page:/>',                            handler= admin_mod.load),
    webapp2.Route('/' + config.get_config('admin') + '/<module:/[w]+>/<page:/[\w]+>',                   handler= admin_mod.load),
    webapp2.Route('/' + config.get_config('admin') + '/<module:/>/<page:/>/<action:/>',                 handler= admin_mod.load),
    webapp2.Route('/' + config.get_config('admin') + '/<module:/[\w]+>/<page:/[\w]+>/<action:/[\w]+>',  handler= admin_mod.load),
    webapp2.Route('<module:/>',                                                                         handler= front_mod.load),
    webapp2.Route('<module:/[\w]+>',                                                                    handler= front_mod.load),
    webapp2.Route('<module:/>/<page:/>',                                                                handler= front_mod.load),
    webapp2.Route('<module:/[w]+>/<page:/[\w]+>',                                                       handler= front_mod.load),
    webapp2.Route('<module:/>/<page:/>/<action:/>',                                                     handler= front_mod.load),
    webapp2.Route('<module:/[\w]+>/<page:/[\w]+>/<action:/[\w]+>',                                      handler= front_mod.load)
], debug=os.environ.get('SERVER_SOFTWARE', '').startswith('Dev'))
