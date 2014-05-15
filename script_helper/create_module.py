#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import config
#
# structure des dossiers a créer
#
# dossier racine
root_folder = {'folders': ['controllers', 'libs', 'locale', 'medias', 'models', 'test', 'views'], 'files': ['__init__.py']}
# dossier des controllers
controllers_folder = {'folders': [], 'files': ['main.py', '__init__.py']}
# dossier des libraies
libs_folder = {'folders': [], 'files': ['__init__.py']}
# dossier des medias
medias_folder = {'folders': ['css', 'js', 'img'], 'files': []}
# dossier des models
models_folder = {'folders': [], 'files': ['__init__.py']}
# dossier des tests
test_folder = {'folders': [], 'files': ['__init__.py']}
# dossier des vues
views_folder = {'folders': ['ajax', 'errors', 'static'], 'files': []}

continu = True
while continu == True:
    print('----| type de modules a créer |----')
    print('1 => admin')
    print('2 => front')
    module_type = input('type de module a créer ? ')
    print('----| création de nouveaux modules |----')
    # nom du module a créer
    module_name = raw_input('nom du nouveau module : ')
    #
    # génération du module
    #
    if str(module_type) == '1':
        path_folder = config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.ADMIN_FOLDER
    else:
        path_folder = config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.FRONT_FOLDER

    # initialisation de la ligne de commande finale
    os.system('sudo chmod 700 -R ' + config.PROJECT_SRC) 
    print('création du dossier pour le module ' + str(module_name))
    os.system('cd ' + path_folder + ' && mkdir ' + module_name + ' && cd ' + module_name)
    # traitement des dossiers et sous-dossiers a créer a partir de la racine du module
    if len(root_folder['folders']) > 0:
        # parcour de l liste des dossiers a créer a la racine
        for elt in root_folder['folders']:
            if elt == 'locale':
                print('\t' + 'création du dossier locale')
                os.system('cd ' + path_folder + ' && cd ' + module_name + ' && mkdir locale')
                for elt in os.listdir(config.PROJECT_SRC + os.sep + 'core' + os.sep + 'locale'):
                    print('\t' + '\t' + 'création du dossier de langue ' + str(elt))
                    os.system('cd ' + path_folder + os.sep + module_name + os.sep + 'locale && mkdir ' + elt)
                    os.system('cd ' + path_folder + os.sep + module_name + os.sep + 'locale' + os.sep + elt + ' && mkdir LC_MESSAGES')
                    os.system('cd ' + path_folder + os.sep + module_name + os.sep + 'locale' + os.sep + elt + os.sep + 'LC_MESSAGES && echo \'msgid ""\nmsgstr ""\n\' > messages.po')
            else:
                print('\t' + 'création du dossier ' + str(elt))
                os.system('cd ' + path_folder + os.sep + module_name + ' && mkdir ' + elt)
                # appel de la variable représentant le sous-dossier
                var_folder = locals()[elt + '_folder']
                if len(var_folder['folders']) > 0:
                    # parcour des sous-dossiers a créer
                    for elt2 in var_folder['folders']:
                        print('\t' + '\t' + 'création du dossier de langue ' + str(elt2))
                        os.system('cd ' + path_folder + os.sep + module_name + os.sep + elt + ' && mkdir ' + elt2)
                if len(var_folder['files']) > 0:
                    # parcour des fichiers a créer dans les dossiers
                    for elt3 in var_folder['files']:
                        print('\t' + '\t' + 'création du dossier de langue ' + str(elt3))
                        os.system('cd ' + path_folder + os.sep + module_name + os.sep + elt + ' && mkdir ' + elt3)

    # traitement des fichiers a créer a la racine
    if len(root_folder['files']) > 0:
        # retour au dossier racine des modules
        for elt in root_folder['files']:
            print('\t' + 'création du dossier ' + str(elt))
            os.system('cd ' + path_folder + ' && touch ' + elt)
    # mise en place d'un chmod 777 pour tous les pojets
    os.system('chmod 777 -R ' + config.PROJECT_SRC)

    if os.path.isdir(path_folder + os.sep + module_name):
        print('le module ' + module_name + ' a bien été créé')
    else:
        print('le module ' + module_name + ' n\'as pas été créé')

    c = raw_input('créer un autre module ? [Y/N] ')
    if c == 'N' or c == 'n':
        continu = False
    else:
        continu = True
