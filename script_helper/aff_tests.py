#! /usr/bin/python
# -*- coding: utf-8 -*-
import webbrowser
import config
import os

print('----| choix du test unitaire a lancer |----')
test = 'y'
while test == 'y':
  aff = raw_input('ouvrir l\'interface web ? (y/n) ')

  if aff == 'y':
    webbrowser.open('http://localhost:8080' + os.sep + config.PROJECT_TESTS)
    print('----------| ouverture de l\'onglet d\'administration de l\'application ' + config.APP_NAME + ' |----------')
  else:
    print('----| type de modules a tester |----')
    print('1 => admin')
    print('2 => front')
    module_type = raw_input('type de module a tester ? ')

  if module_type == '1':
    for elt in os.listdir(config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.ADMIN_FOLDER + os.sep):
      if os.path.isdir(config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.ADMIN_FOLDER + os.sep + elt):
        print(elt)

    sel_mod = raw_input('quel module souhaitez vous tester ? ')

    for elt in os.listdir(config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.ADMIN_FOLDER + os.sep + sel_mod + '/test/'):
      if elt != '__init__.py' and os.path.isfile(config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.ADMIN_FOLDER + os.sep + sel_mod + '/test/' + elt): 
        print(elt[0:len(elt) - 3])

  if module_type == '2':
    for elt in os.listdir(config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.FRONT_FOLDER + os.sep):
      if os.path.isdir(config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.FRONT_FOLDER + os.sep + elt):
        print(elt)

    sel_mod = raw_input('quel module souhaitez vous tester ? ')

    for elt in os.listdir(config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.FRONT_FOLDER + os.sep + sel_mod + '/test/'):
      if elt != '__init__.py' and os.path.isfile(config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.FRONT_FOLDER + os.sep + sel_mod + '/test/' + elt): 
        print(elt[0:len(elt) - 3])

  sel_test = raw_input('quel test souhaitez vous exécuter ? ')

  os.system('cd ' + config.PROJECT_SRC + '/aeta && python local_client.py ' + config.URL_ACCES + config.PROJECT_TESTS +' modules.'+ str(sel_mod) +'.test.' + str(sel_test))
  
  test = raw_input('souhaitez vous lancer un autre tests ? (y/n) ')