# -*- coding: utf-8 -*-
import os
import webbrowser
import subprocess

import config

print('----| lancement de l\'application |----')

root_project = config.PROJECT_SRC + '/'

update       = raw_input('mettre à jour le système d\'exploitation (linux only) ? (y/n) ')
editeur      = raw_input('ouvrir l\'éditeur de texte ? (y/n) ')
explorer     = raw_input('ouvrir l\'explorer de fichiers ? (y/n) ')
onglet_site  = raw_input('ouvrir l\'onglet du site dans le navigateur ? (y/n) ')
onglet_back  = raw_input('ouvrir l\'onglet du panel dans le navigateur ? (y/n) ')

if os.path.isfile(config.PROJECT_DOC):
  doc        = raw_input('ouvrir la documentation du projet ? (y/n) ')
else:
  doc        = 'n'

onglet_tests  = raw_input('afficher les tests unitaires ? (y/n) ')

if update == 'y':
  print('----------| début de mise à jour du système |----------')
  print('\n'+'\t'+'----------| mise a jour des références de paquets |----------')
  os.system('sudo yum update -y')
  print('\n'+'\t'+'----------| mise a jour des paquets |----------')
  os.system('sudo yum upgrade -y')
  os.system('exit')
  print('----------| fin de mise à jour du système |----------')

os.system('sudo chmod -R 700 ' + config.PROJECT_PATH + ' && cd ' + config.PROJECT_HELP + ' && python launch_serv.py')

if editeur     == 'y':
  subprocess.Popen(config.TEXT_EDITOR_PROCESS)
  print('----------| ouverture de ' + config.TEXT_EDITOR_NAME + ' |----------')

if explorer    == 'y':
  os.system('thunar ' + config.PROJECT_PATH)
  print('----------| ouverture du dossier contenair |----------')

if onglet_site == 'y':
  webbrowser.open('http://localhost:8080')
  print('----------| ouverture de l\'application ' + config.APP_NAME + ' |----------')

if onglet_back == 'y':
  webbrowser.open('http://localhost:8000')
  print('----------| ouverture de l\'onglet d\'administration de l\'application ' + config.APP_NAME + ' |----------')

if doc         == 'y':
  webbrowser.open(config.PROJECT_DOC)
  print('----------| ouverture de le la documentation de ' + config.APP_NAME + ' |----------')

if onglet_tests == 'y':
  os.popen('sudo chmod -R 700 ' + config.PROJECT_PATH + ' && cd ' + config.PROJECT_HELP + ' && python aff_tests.py')