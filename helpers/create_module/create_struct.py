#!/usr/bin/env python
# -*- coding: utf-8 -*-
# disco-toolbox-2.helpers.create_module.create_struct -- fichier de création des structure des modules

import os
import shutil
try:
    import yaml                                                                                                                                 # import de la librairie yaml dans le cas d'un appel depuis le dossier helpers
except:
    from helpers import yaml                                                                                                                    # import de la librairie yaml dans le cas d'un appel depuis le fichier d'installation

from helpers import clean_app

def create_struct(path, module_name, mod_folder, lang, home_page, home_class):
    """fonction de création des dossiers et fichiers du module
    :param path:        chemin du dossier module
    :param module_name: nom du module a créer
    :param mod_folder:  nom du dossier contenant les modules
    :param lang: code   langue par défaut du site
    :param home_page:   nom du controlleur d'accueil par défaut du module
    :param home_class:  nom de la classe d'accueil par défaut du controller
    :returns:           renvoi le chemin relatif du script
    :rtype:             affichage
    """
    if str(os.getcwd()[len(os.getcwd()) - 7:len(os.getcwd())]) == 'install':
        f = open(os.getcwd()[0:len(os.getcwd()) - 7] + os.sep + 'helpers' + os.sep + 'create_module' + os.sep + 'struct_module.yaml', 'r')      # ouverture du fichier struct_module.yaml appelé depuis un script du dossier d'installation
    elif str(os.getcwd()[len(os.getcwd()) - 7:len(os.getcwd())]) == 'helpers':
        f = open(os.getcwd() + os.sep + 'create_module' + os.sep + 'struct_module.yaml', 'r')                                                   # ouverture du fichier struct_module.yaml appelé depuis le script de création de modules
    else:
        f = open(os.getcwd() + os.sep + 'helpers' + os.sep + 'create_module' + os.sep + 'struct_module.yaml', 'r')        

	docs = yaml.load(f)                                                                                                                         # fermeture du fichier struct_module.yaml
	if os.path.isdir(path + os.sep + module_name):
		shutil.rmtree(path + os.sep + module_name)
		print('suppression de l\'ancien module ' + path + os.sep + module_name + '.' * 15 + ' done')

    os.mkdir(path + os.sep + module_name)                                                                                                       # création du fichier racine du module
    print('création du module ' + path + os.sep + module_name + '.' * 15 + ' done')

    for f in docs['root'][0]['folders']:                                                                                                        # parcours de la liste des dossiers devant être présent a la racine
        os.mkdir(path + os.sep + module_name + os.sep + f)                                                                                      # création des sous-dossiers
        if f == 'locale':                                                                                                                       # cas du dossier local
            for s_f in docs['locale'][0]['folders']:                                                                                            # parcours de ses sous-dossiers
                target_root_folder = path + os.sep + module_name + os.sep + 'locale' + os.sep + lang                                            # création du chemin du sous-dossier de langue
                try:                                                                                                                            # vérification de l'existence du dossier pour afficher son état de création
                    os.mkdir(target_root_folder)                                                                                                # création de ses sous-dossiers
                    print('création du dossier ' + target_root_folder + '.' * 15 + ' done')
                except:
                    print('création du dossier ' + target_root_folder + '.' * 15 + ' failed')

                target_folder = target_root_folder + os.sep + s_f                                                                               # création du chemin du sous-dossier LC_MESSAGES dans le dossier de langue
                
                try:                                                                                                                            # vérification de sons état
                    os.mkdir(target_folder)                                                                                                     # création du sous-dossier
                    print('création du dossier ' + target_folder + '.' * 15 + ' done')
                except:
                    print('création du dossier ' + target_folder + '.' * 15 + ' failed')

            for s_f in docs['locale'][1]['files']:                                                                                              # parcours de la liste des fichiers devant être présent a la racine
                target_file = target_root_folder + os.sep + docs['locale'][0]['folders'][0] + os.sep + s_f                                      # création du chemin du fichier
                
                try:                                                                                                                            # vérification de l'état du fichier
                    app_file    = open(target_file, 'wb')                                                                                       # création du fichier
                    app_file.close()
                    print('création du fichier ' + target_file + '.' * 15 + ' done')
                except:
                    print('création du fichier ' + target_file + '.' * 15 + ' failed')

        else:
            for s_f in docs[f][0]['folders']:                                                                                                   # parcours de ses sous-dossiers
                target_folder = path + os.sep + module_name + os.sep + f + os.sep + s_f                                                         # génération du chemin du dossier

                try:                                                                                                                            # vérification de l'état du fichier
                    os.mkdir(target_folder)                                                                                                     # création de ses sous-dossiers
                    print('création du dossier ' + target_folder + '.' * 15 + ' done')
                except:
                    print('création du dossier ' + target_folder + '.' * 15 + ' failed')

            for s_f in docs[f][1]['files']:                                                                                                     # parcours des fichiers a créer
                target_file = path + os.sep + module_name + os.sep + f + os.sep + s_f                                                           # génération du chemin

                try:                                                                                                                            # test du fichier en cours de traitements
                    app_file    = open(target_file, 'wb')# génration du fichier
                    app_file.write('')                                                                                                          # générationd u contenu vide
                    app_file.close()                                                                                                            # fermeture du fichier
                    print('création du fichier ' + target_file + '.' * 15 + ' done')
                except:
                    print('création du fichier ' + target_file + '.' * 15 + ' failed')

                if f == '<cont></cont>rollers':                                                                                                          # test du fossier en cours de traitement
                    target_controller = path + os.sep + module_name + os.sep + f + os.sep + home_page + '.py'                                   # génération du chemin du controller d'accès par défault
                    try:# test de l'état du controller créé
                        app_file = open(target_controller, 'wb')                                                                                # générataion du controller
                        """
                        génération du contenu du main controller
                        """
                        content  = '#!/usr/bin/env python' + '\n'
                        content  += '# -*- coding: utf-8 -*-' + '\n'
                        content  += '# disco-toolbox-2.src.' + mod_folder + '.' + f + '.' + home_page + ' -- controller principal du module ' + f 
                        content  += '\n' + '\n'
                        content  += 'import webapp2'
                        content  += '\n' + '\n'
                        content  += 'class ' + home_class + '(webapp2.RequestHandler):' + '\n'
                        content  += '\t' + 'def get(self):' + '\n'
                        content  += '\t' + '\t' + 'self.response.write(\'Hello world ' + module_name + ' !\')'
                        content  += '\n' + '\n'
                        content  += '\t' + 'def post(self):' + '\n'
                        content  += '\t' + '\t' + 'self.response.write(\'Hello world ' + module_name + ' !\')' + '\n'
                        app_file.write(content)
                        app_file.close()
                                                                     
                        print('création du fichier ' + target_controller + '.' * 15 + ' done')
                    except:
                        print('création du fichier ' + target_controller + '.' * 15 + ' failed')

    print('création du dossier du module ' + module_name + ' ' + '.' * 15 + ' done')
