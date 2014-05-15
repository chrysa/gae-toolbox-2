#! /usr/bin/python
# -*- coding: utf-8 -*-
import os

APPENGINE        	= '/home/chrysa/google_appengine'                                  # chemin d'accès aux dossier appengine
URL_ACCES			= 'http://localhost:8080/'
APP_NAME         	= 'disco-gae-toolbox'                                              # nom du dossier contenant l'application
APP_FOLDER_NAME  	= 'disco-gae-toolbox'                                              # nom de l'application
LANG             	= 'fr_FR'                                                          # langue du site par défault
MODULES_FOLDER   	= 'modules'   		                                               # nom du dossier contenant les modules
ADMIN_FOLDER   		= 'admin'	
FRONT_FOLDER   		= 'front'	
TEXT_EDITOR_PROCESS = 'sublime_text'                                                   # nom du processus correspondant a l'éditeur de texte a lancer
TEXT_EDITOR_NAME 	= 'sublime text 2'                                                 # nom de l'éditeur de texte a lancer

PROJECT_PATH     	= os.path.dirname(__file__)[0:len(os.path.dirname(__file__)) - 14] # chemin racine du projet
PROJECT_DOC      	= PROJECT_PATH + '/doc/index.html'                                 # chemin d'accès a la documention du sites
PROJECT_HELP      	= PROJECT_PATH + '/script_helper'                                  # chemin d'accès au dossier des scripts d'help du sites
PROJECT_SRC      	= PROJECT_PATH + '/src'                                            # chemin d'accès au dossier des sources du sites
PROJECT_TESTS		= 'tests/' 			                                           	   # nom de l'argument a passer en URLS pour accéder aux tests unitaires	