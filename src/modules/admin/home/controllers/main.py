#!/usr/bin/env python
# -*- coding: utf-8 -*-
# disco-toolbox-2.src.modules.controllers.main -- controller principal du module controllers

import webapp2

class main(webapp2.RequestHandler):
	def get(self):
		self.response.write('Hello world home !')

	def post(self):
		self.response.write('Hello world home !')
