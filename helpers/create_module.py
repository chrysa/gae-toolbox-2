#!/usr/bin/env python
# -*- coding: utf-8 -*-
# disco-toolbox-2.helpers.create_module -- fichier de création de module

import os
import yaml

from create_module import create_struct                                                                                    # appel du fichier de création de modules
from create_module import find_path                                                                                        # appel du fichier de génération du chemin

f = open(os.getcwd()[0:len(os.getcwd()) - 8] + os.sep + 'src' + os.sep + 'config.yaml', 'r')                               # ouverture du fichier yaml de configuration
doc = yaml.load(f)                                                                                                         # chargement du fichier yaml
"""
procédure de création
"""
continu = True
while continu == True:
    print('----| type de modules a créer |----')
    print('1 => admin')
    print('2 => front')
    module_type = input('type de module a créer ? ')
    print('----| création de nouveaux modules |----')
    # nom du module a créer
    module_name = raw_input('nom du nouveau module : ')
    target = find_path.find_path(module_type, doc['mod_folder'])                                                           # récupération du chemin
    create_struct.create_struct(target, module_name, doc['mod_folder'], doc['lang'], doc['home_page'], doc['home_class'])  # création du module
    c = raw_input('créer un autre module ? [Y/N] ')
    if c == 'N' or c == 'n':
        continu = False
    else:
        continu = True
