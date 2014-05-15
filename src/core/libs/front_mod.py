#!/usr/bin/env python
# -*- coding: utf-8 -*-

 # -*- coding: utf-8 -*-
# disco-toolbox.src.core.controllers.mod -- fichier de gestion d'appel des modules et de leurs mmédias
import os
import logging

import webapp2

from core             import config                                                                                     	        # import du fichier de config
from core.controllers import ErrorsController                                                               				        # fichier de gestion des erreurs HTTP


def formate_module(module):
	"""fonction de récupération du nom du module débarassé de slashs
	:param module:     nom du module appelé
	:returns:          nom du module formaté
	:rtype:            string
	"""
	if module == '/':
	    module = config.FRONT_HOME
	else:
	    module = module[1:len(module)]                                                                      				        # suppression du premier slash
	    if module[(len(module) - 1):len(module)] == '/':                                                    				        # test de la présence d'un slash en fin de chaine
	        module = module[1:len(module)]                                                                  				        # récupération de la chaine sans le slash final
	return module

def list_mod(url):
	"""fonction de génération de la liste des modules présents et pouvant être appelé via l'URL
	:param url:        accès au module via l'URL
	:returns:          la liste des modules présents chemin d'accès relatif a la feuille de style
	:rtype:            liste
	"""
	lst = os.listdir(config.FRONT_PATH)                                                				        # génération de la liste des modules présents
	print(config.FRONT_PATH)
	liste = []
	for d in lst:
	    if url == '1':                                                                                      						# vérificaion de l'accès via URL
	        if d not in config.MODULES_BLACKLIST:                                                           						# vérification de l'accessibilité des modules
	            s = config.FRONT_PATH + os.sep + d                                                        						# génération du chemein relatif du module en cours de traitement
	            if os.path.isdir(s) and os.path.exists(s + os.sep + "__init__.py"):                         						# vérification de la validité du module
	                liste.append(d)                                                                          						# ajout du module dans la liste

	return liste

def is_mod(module):
	"""fonction de test d'existence d'un module
	:param module:	nom du module a tester
	:returns:		retourne l'état d'existence du module
	:rtype:			booléen
	"""
	if os.path.isdir(config.FRONT_PATH + module):
		return True
	else:
		return False

def is_controller_page(module, page):
	"""fonction de test d'existence d'une page
	:param module:	nom du module a tester
	:param t:		type de fichier a tester
	:param page:	nom de la page a tester
	:returns:		retourne l'état d'existence de la page cible
	:rtype:			booléen
	"""
	if os.path.isfile(config.FRONT_PATH + module + '/controllers/' + page + '.py'):
		return True
	else:
		return False

def is_model_page(module, page):
	"""fonction de test d'existence d'une page
	:param module:	nom du module a tester
	:param t:		type de fichier a tester
	:param page:	nom de la page a tester
	:returns:		retourne l'état d'existence de la page cible
	:rtype:			booléen
	"""
	if os.path.isfile(config.FRONT_PATH + module + '/models/' + page + '.py'):
		return True
	else:
		return False

def is_fct(obj, fct):
	"""fonction de test d'existence d'un attribut dans l'objet
	:param module:	nom de l'attribut a tester
	:returns:		retourne l'état d'existence de l'attribut cible
	:rtype:			booléen
	"""
	if hasattr(obj, fct):
		return True
	else:
		return False		

def load_controller(module, controller):
	mod = __import__(config.MODULES_FOLDER + '.' + config.MODULES_FRONT_FOLDER + '.' + module + '.controllers.' + controller, fromlist=[controller])
	return mod

def load_model(module, model):
	mod = __import__(config.MODULES_FOLDER + '.' + config.MODULES_FRONT_FOLDER + '.' + module + '.models.' + model, fromlist=[model])
	return mod

class GetModuleCSS(webapp2.RequestHandler):
	"""class de gestion des CSS"""
	def get(self, module, css):
		"""fonction de récupération de fichiers CSS d'un module
		:param module:     le nom du module cible
		:param css:        nom de la page css
		:returns:          chemin d'accès relatif à la feuille de style
		:rtype:            string
		"""
		print(module)
		print(css)
		file_path = config.PROJECT_PATH + config.MODULES_FRONT_FOLDER + os.sep + module + 'medias' + os.sep + 'css' + os.sep + css + '.css'
		if module != '' or os.path.exists(file_path):
		    return file_path
		else:
		    return config.PROJECT_PATH + config.MODULES_FRONT_FOLDER + os.sep + config.FRONT_HOME + 'medias' + os.sep + 'css' + os.sep + css + '.css'

class GetModuleImg(webapp2.RequestHandler):

	"""class de gestion des images"""
	def get(self, module, img):
	    """fonction de récupération des images d'un module
	    :param module:     le nom du module cible
	    :param img:        nom et extenssion de l'image
	    :returns:          chemin d'accès relatif à l'image
	    :rtype:            string
	    """
	    return config.PROJECT_PATH + config.MODULES_FRONT_FOLDER + os.sep + module + os.sep + 'medias' + os.sep + 'img' + img

class GetModuleJS(webapp2.RequestHandler):

	"""class de gestion des JS"""
	def get(self, module, js):
	    """fonction de récupération de fichiers JS d'un module
	    :param module:     le nom du module cible
	    :param js:         nom de la page js
	    :returns:          chemin d'accès relatif au script JS
	    :rtype:            string
	    """
	    file_path = config.PROJECT_PATH + config.MODULES_FRONT_FOLDER + os.sep + module + 'medias' + os.sep + 'js' + os.sep + js + '.j'
	    if module != '' or os.path.exists(file_path):
	        return file_path
	    else:
	        return config.PROJECT_PATH + config.MODULES_FRONT_FOLDER + os.sep + config.FRONT_HOME + 'medias' + os.sep + 'js' + os.sep + js + '.js'
	        
class load(webapp2.RequestHandler):
	"""class de gestion des modules pour le chargement a la volée"""
	def get(self, module=config.FRONT_HOME, page=config.HOME_PAGE, fct=config.HOME_CLASS, url='1'):
		"""fonction de chargements de modules a la volée via un appel par GET
		:param module: nom du module a charger
		:param page:   nom de la page cible
		:param fct:    nom de la fonction a appeller
		:param url:    défini si l'appel vient de l'url ou pas
		:returns:      retournes la page demandée ou une erreur
		"""
		module = formate_module(module)																					# formatage des modules
		if module in list_mod(url) and is_mod(module) and is_controller_page(module, page): 	
			mod = load_controller(module, page)
			if is_fct(mod, fct):
				cls = getattr(mod, fct)
			else:
				cls =getattr(mod,config.HOME_CLASS)
			cls().get(self)
		else:
		  	ErrorsController.handle_404(self.request, self.response, logging.exception)                     				        # appel d'une 404 dans le cas d'un module non autorisé

	def post(self, module=config.FRONT_HOME, page=config.HOME_PAGE, fct=config.HOME_CLASS, url='1'):
		"""fonction de chargements de modules a la volée via un appel par POST
		:param module: nom du module a charger
		:param page:   nom de la page cible
		:param fct:    nom de la fonction a appeller
		:param url:    défini si l'appel vient de l'url ou pas
		:returns:      retournes la page demandée ou une erreur
		"""
		module = formate_module(module)																								# formatage des modules
		if module in list(url) and is_mod(module) and is_controller_page(module, page): 
			mod = load_controller(module, page)
			if is_fct(mod, fct):
				cls = getattr(mod, fct)
			else:
				cls =getattr(mod,config.HOME_CLASS)
			cls().post(self)
		else:
		  	ErrorsController.handle_404(self.request, self.response, logging.exception)                     				        # appel d'une 404 dans le cas d'un module non autorisé
