#!/usr/bin/env python
# -*- coding: utf-8 -*-
# disco-toolbox-2.install -- fichier d'installation de disco-toolbox

import os
import sys

from install import gen_app_yaml
from install import gen_config_yaml

import helpers

from helpers import yaml
from helpers import clean_app

from helpers.create_module import create_struct
from helpers.create_module import find_path

path = os.getcwd()                                                                                                                                  # récupération du chemin du dossier d'applicaton
src_path = path + os.sep + 'src' + os.sep                                                                                                           # génération du chemin du dossier des sources
install_path = path + os.sep + 'install' + os.sep                                                                                                   # génération du chemin du dossier des installations
conf = {}                                                                                                                                           # initialisation du dictionnaire contenant les paramètres de configuration

print('-' * 54)
print('installation de gae-toolbox')
print('-' * 54)
print('-' * 5 + ' step 1/9 : paramétrage du fichier app.yaml ' + '-' * 5)
app_name                      = raw_input('nom de l\'application : ')                                                                               # récupération du nom de l'aplication

print('-' * 5 + ' step 2/9 : paramétrage du fichier config.yaml : configuration générale ' + '-' * 5)
conf['SITE_TITLE'] 			  = raw_input('titre du site : ')                                                                                                  # récupération du titre du site
conf['NDD']                   = raw_input('nom de domaine de l\'application : ')                                                                    # récupération du nom de domaine utilisé pour le déployement de l'application
conf['TIMEZONE']              = raw_input('timezone par défault : [Europe/Paris] ')                                                                 # récupération de la timezone par ddéfaut du site
conf['LANG']                  = raw_input('langue par défault du site : [fr_FR] ')                                                                  # récupération du code langue par défault
conf['DEFAULT_MEMCACHE_TIME'] = raw_input('temps de mise en memcache des données : [10] ')                                                          # récupération du temps de stockage des données en memcache
conf['ADMIN_ZONE_URL']        = raw_input('route d\'accès a la zone d\'administration : [admin] ')                                                 # récupération de la route d'accès a la zone d'administration8

print('-' * 5 + ' step 3/9 : paramétrage du fichier config.yaml : configuration des contacts ' + '-' * 5)
conf['ENVOI_CONTACT']         = raw_input('adresse de messagerie d\'envoi des mails : ')                                                            # récupération de l'adresse d'expédition des mails
conf['RECEPTION_CONTACT']     = raw_input('adresse de messagerie de réception des mails : ')                                                        # récupération de l'adresse de réception des mails

print('-' * 5 + ' step 4/9 : paramétrage du fichier config.yaml : configuration générale des modules ' + '-' * 5)
conf['MODULES_FOLDER']        = raw_input('nom du dossier contenant les modules : [modules] ')                                                      # récupération du nom du dossier contenant les modules
conf['FRONT_HOME']            = raw_input('nom du module d\'accueil des utilisateurs : [home] ')                                                    # récupération du nom du module d'accueil des utilisteurs
conf['ADMIN_HOME']            = raw_input('nom du module d\'accueil du panel d\'administration : [home] ')                                          # récupération du nom du module d'accueil du staff
conf['HOME_PAGE']             = raw_input('nom du controllers appelé par défault : [main] ')                                                        # récupération du nom du controller par défault
conf['HOME_CLASS']            = raw_input('nom de la class appelée par défault : [main] ')                                                          # récupration de la class par défault

print('-' * 5 + ' step 5/9 : paramétrage du fichier config.yaml : configuration des modules inaccessible par URL pour les utilisateurs ' + '-' * 5)
conf['MODULES_BLACKLIST']     = raw_input('liste des modules insaccessible via URL (séparé par une virgule) ')                                      # récupérationde modules blacklisté pour les accès direct

print('-' * 5 + ' step 6/9 : configuration du fichier app.yaml ' + '-' * 5)
if app_name != '':                                                                                                                                  
    gen_app_yaml.gen_app_yaml(app_name, install_path, src_path)                                                                                     # génération du fichier app.yaml
else:                                                                                                                                               
    sys.exit('vous devez saisir le nom de l\'application')

print('-' * 5 + ' step 7/9 : configuration du fichier config.yaml ' + '-' * 5)
gen_config_yaml.gen_config_yaml(conf, src_path)                                                                                                     # génération du fichier config.yaml

print('-' * 5 + ' step 8/9 : configuration des fichiers système ' + '-' * 5)

f    = open(os.getcwd() + os.sep + 'src' + os.sep + 'config.yaml', 'r')
conf = yaml.load(f)

print('-' * 5 + ' step 9/9 : ccréation des modules de base ' + '-' * 5)
print('génération du module d\'accueil des utilisateurs ' + '.' * 60 + ' please wait')

path = find_path.find_path(0, conf['mod_folder'])                                                                                                 # recuperation du chemin du front
helpers.clean_app;

print('génération du module d\'accueil de la zone d\'administration ' + '.' * 60 + ' please wait')
path = find_path.find_path(1, conf['mod_folder'])                                                                                                 # recuperation du chemin du pannel
create_struct.create_struct(path, conf['admin_home'], conf['mod_folder'], conf['lang'], conf['home_page'], conf['home_class'])                    # création du module d'accueil du panel

if os.path.isfile(src_path + 'app.yaml') and os.path.isfile(src_path + 'config.yaml'):
    print('configuration complète ' + '.' * 42 + ' complete')
else:
    print('configuration complète ' + '.' * 42 + ' failed')
os.system("pause")
