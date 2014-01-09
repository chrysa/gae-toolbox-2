#!/usr/bin/env python
# -*- coding: utf-8 -*-
# disco-toolbox-2.helpers.find_path -- fichier de génération du chemin relatif du script en cours d'éxécution

import os


def find_path(module_type, mod_folder):
    """fonction de génération du chemin relatif du script en cours d'éxécution
    :param module_type: type de module
    :param mod_folder:  nom du dossier contenant les modules admin et front 
    :returns:           renvoi le chemin relatif du script
    :rtype:             string
    """
    test = os.getcwd()[len(os.getcwd()) - 7:len(os.getcwd())]                                                           # isolation des 8 derniers caractères permettant de savoir si le script est appelé depuis le dossier d'installation

    if module_type == 1:
        if test == 'install' or test == 'helpers':
            path_folder = os.getcwd()[0:len(os.getcwd()) - 8] + os.sep + 'src' + os.sep + mod_folder + os.sep + 'admin'
        else:
            path_folder = os.getcwd() + os.sep + 'src' + os.sep + mod_folder + os.sep + 'admin'
    else:
        if test == 'install' or test == 'helpers':
            path_folder = os.getcwd()[0:len(os.getcwd()) - 8] + os.sep + 'src' + os.sep + mod_folder + os.sep + 'front'
        else:
            path_folder = os.getcwd() + os.sep + 'src' + os.sep + mod_folder + os.sep + 'front'

    return path_folder
