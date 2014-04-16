#!/usr/bin/env python
# -*- coding: utf-8 -*-
# disco-toolbox.src.core.front_mod -- fichier de gestion d'appel des modules du front


import webapp2

class load(webapp2.RequestHandler):
	"""class de gestion des modules pour le chargement a la volée"""
	def get(self, module='1', page='1', fct='1'):
		print('plop front')