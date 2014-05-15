# -*- coding: utf-8 -*-
# disco-toolbox.src.core.controllers.ErrorsController -- fichier de gestion d'affichage des erreurs HTTP
import logging
import os

from core import config                                                                         # import du fichier de config
from core.libs import affichage
from core.libs import internationalize                                                          # import du fichier de gestion des traductions

SITE_TITLE = config.SITE_TITLE                                                                  # titre du site
SITE_URL   = config.SITE_URL                                                                    # URL d'accès au site

TRAD_PATH  = config.PROJECT_PATH + os.sep + 'core' + os.sep + 'locale'                          # chemin d'accès au dossier des traductions


def handle_403(request, response, exception) :
	"""fonction d'affichage de la page d'erreur 403 custom
	:param request:   request de l'objet en cours de traitement
	:param reponse:   response de l'objet en cours de traitement
	:param exception: exception généré par le module logging
	:returns:         affichage de l'erreur
	"""
	internationalize.trad_conf(TRAD_PATH, request)                                              # intialisation de la traduction pour l'erreur
	logging.exception(exception)                                                                # recupération de l'exception
	template_page_head = affichage.GetErrorView('403_head')                              		# récupération du gabarit de la 403 custom
	template_page_content = affichage.GetErrorView('403_content')                           	# récupération du gabarit de la 403 custom
	template_values_head = {
		'title' : SITE_TITLE + ' : ' + internationalize.trad('title_403'),
		'tempo' : '30',
		'host' : SITE_URL
	}
	template_values_content = {
		'error' : internationalize.trad('err_403'),
		'message' : internationalize.trad('mess_403')
	}
	content = {
		'head' : affichage.code_render(template_page_head, template_values_head),
		'content' : affichage.code_render(template_page_content, template_values_content)
	}
	affichage.extend_to_base(response, content)
	response.set_status(403)


def handle_404(request, response, exception) :
	"""fonction d'affichage de la page d'erreur 404 custom
	:param request:   request de l'objet en cours de traitement
	:param reponse:   response de l'objet en cours de traitement
	:param exception: exception généré par le module logging
	:returns:         affichage de l'erreur
	"""
	internationalize.trad_conf(TRAD_PATH, request)                                              # intialisation de la traduction pour l'erreur
	logging.exception(exception)                                                                # recupération de l'exception
	template_page_head = affichage.GetErrorView('404_head')                         			# récupération du gabarit de la 404 custom
	template_page_content = affichage.GetErrorView('404_content')                      			# récupération du gabarit de la 404 custom
	template_values_head = {
		'title' : SITE_TITLE + ' : ' + internationalize.trad('title_404'),
		'tempo' : '5',
		'cible' : SITE_URL,
	}
	template_values_content = {
		'message_clic' : internationalize.trad('mess_clic_404'),
		'cible' : SITE_URL,
		'error' : internationalize.trad('err_404'),
		'message' : internationalize.trad('mess_404')
	}
	content = {
		'head' : affichage.code_render(template_page_head, template_values_head),
		'content' : affichage.code_render(template_page_content, template_values_content)
	}
	affichage.extend_to_base(response, content)
	response.set_status(404)


def handle_500(request, response, exception) :
	"""fonction d'affichage de la page d'erreur 500 custom
	:param request:   request de l'objet en cours de traitement
	:param reponse:   response de l'objet en cours de traitement
	:param exception: exception généré par le module logging
	:returns:         affichage de l'erreur
   """
	internationalize.trad_conf(TRAD_PATH, request)                                              # intialisation de la traduction pour l'erreur
	logging.exception(exception)                                                                # recupération de l'exception
	template_page_head = affichage.GetErrorView('500_head')                              		# récupération du gabarit de la 500 custom
	template_page_content = affichage.GetErrorView('500_content')                           	# récupération du gabarit de la 500 custom
	template_values_head = {
		'title' : SITE_TITLE + ' : ' + internationalize.trad('title_500'),
	}
	template_values_content = {
		'error' : internationalize.trad('err_500'),
		'message' : internationalize.trad('mess_500'),
	}
	content = {
		'head' : affichage.code_render(template_page_head, template_values_head),
		'content' : affichage.code_render(template_page_content, template_values_content)
	}
	affichage.extend_to_base(response, content)
	response.set_status(500)


def handle_502(request, response, exception) :
	"""fonction d'affichage de la page d'erreur 502 custom
	:param request:   request de l'objet en cours de traitement
	:param reponse:   response de l'objet en cours de traitement
	:param exception: exception généré par le module logging
	:returns:         affichage de l'erreur
	"""
	internationalize.trad_conf(TRAD_PATH, request)                                              # intialisation de la traduction pour l'erreur
	logging.exception(exception)                                                                # recupération de l'exception
	template_page_head = affichage.GetErrorView('502_head')                              		# récupération du gabarit de la 502 custom
	template_page_content = affichage.GetErrorView('502_content')                           	# récupération du gabarit de la 502 custom
	template_values_head = {
		'title' : SITE_TITLE + ' : ' + internationalize.trad('title_502'),
	}
	template_values_content = {
		'error' : internationalize.trad('err_502'),
		'message' : internationalize.trad('mess_502'),
	}
	content = {
		'head' : affichage.code_render(template_page_head, template_values_head),
		'content' : affichage.code_render(template_page_content, template_values_content)
	}
	affichage.extend_to_base(response, content)
	response.set_status(502)


def handle_504(request, response, exception) :
	"""fonction d'affichage de la page d'erreur 504 custom
	:param request:   request de l'objet en cours de traitement
	:param reponse:   response de l'objet en cours de traitement
	:param exception: exception généré par le module logging
	:returns:         affichage de l'erreur
	"""
	internationalize.trad_conf(TRAD_PATH, request)                                              # intialisation de la traduction pour l'erreur
	logging.exception(exception)                                                                # recupération de l'exception
	template_page_head = affichage.GetErrorView('504_head')                              		# récupération du gabarit de la 504 custom
	template_page_content = affichage.GetErrorView('504_content')                           	# récupération du gabarit de la 504 custom
	template_values_head = {
		'title' : SITE_TITLE + ' : ' + internationalize.trad('title_504'),
	}
	template_values_content = {
		'error' : internationalize.trad('err_504'),
		'message' : internationalize.trad('mess_504'),
	}
	content = {
		'head' : affichage.code_render(template_page_head, template_values_head),
		'content' : affichage.code_render(template_page_content, template_values_content)
	}
	affichage.extend_to_base(response, content)
	response.set_status(504)
