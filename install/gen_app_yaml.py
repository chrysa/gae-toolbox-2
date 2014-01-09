#!/usr/bin/env python
# -*- coding: utf-8 -*-
# disco-toolbox-2.install.gen_app_yaml -- fichier de génération du fichier app.yaml

import os


def gen_app_yaml(app_name, install_path, src_path):
    """fonction de génération du fichier app.yaml
    :param app_name:     nom de l'application
    :param install_path: chemin du dossier d'installation
    :param src_path:     chemin du dossier des souces
    """
    print('génération du fichier app.yaml ' + '.' * 60 + ' please wait')
    """
    création du contenu du app.yaml
    """
    app_content = 'application: ' + app_name

    gabarit = open(install_path + 'gabarit_app', 'r+')                                          # ouverture du fichier gabarit
    app_content += gabarit.read()                                                               # récupération du contenu du gabarit
    gabarit.close()                                                                             # fermeture du fichier gabarit

    if os.path.isfile(src_path + 'app.yaml'):
        os.remove(src_path + 'app.yaml')                                                        # suppression du fichier app.yaml si il existe
        if os.path.isfile(src_path + 'app.yaml'):
            print('\t' + 'suppression du fichier app.yaml déjà présent ' + '.' * 20 + ' failed')
        else:
            print('\t' + 'suppression du fichier app.yaml déjà présent ' + '.' * 20 + ' done')

    """
    création du nouveau fichier app.yaml
    """
    app_file = open(src_path + 'app.yaml', 'wb')                                                # création et ouverture du fichier app.yaml
    app_file.write(app_content)                                                                 # remplissage du fichier
    app_file.close()                                                                            # fermeture du fichier

    if os.path.isfile(src_path + 'app.yaml'):
        print('\t' + 'enregistrement du fichier app.yaml ' + '.' * 33 + ' done')
    else:
        print('\t' + 'enregistrement du fichier app.yaml ' + '.' * 33 + ' failed')
