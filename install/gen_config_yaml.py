#!/usr/bin/env python
# -*- coding: utf-8 -*-
# disco-toolbox-2.install.gen_config_yaml -- fichier de génération du fichier config.yaml

import os


def gen_config_yaml(conf, src_path):
    """fonction de génération du fichier config.yaml
    :param app_name:     nom de l'application
    :param install_path: chemin du dossier d'installation
    :param src_path:     chemin du dossier des souces
    """
    if os.path.isfile(src_path + 'config.yaml'):
        os.remove(src_path + 'config.yaml')                                                                 # suppression du fichier de configuration déja existant
        if os.path.isfile(src_path + 'config.yaml'):
            print('suppression du fichier config.yaml déjà présent ' + '.' * 20 + ' failed')
        else:
            print('suppression du fichier config.yaml déjà présent ' + '.' * 20 + ' done')
    print('génération du fichier config.yaml ' + '.' * 60 + ' please wait')

    """
    généaration du contenu
    """
    config_content = 'title: ' + conf['SITE_TITLE'] + '\n'                                                  # génération de la ligne de titre
    print('\t' + 'définition du nom du site ' + '.' * 38 + ' done')
    config_content += 'ndd: ' + conf['NDD'] + '\n'                                                          # génération de la ligne du nom de domaine
    print('\t' + 'définition du nom de domaine ' + '.' * 35 + ' done')
    config_content += 'send_mail: ' + conf['ENVOI_CONTACT'] + '\n'                                          # génération de la ligne d'adresse d'envoi de mails
    print('\t' + 'définition de l\'adresse d\'envoi de mail ' + '.' * 25 + ' done')
    config_content += 'recep_mail: ' + conf['RECEPTION_CONTACT'] + '\n'                                     # génération de la ligne d'adresse de réception de mails
    print('\t' + 'définition de l\'adresse de reception de mail ' + '.' * 19 + ' done')

    if conf['TIMEZONE'] == '':                                                                              # génération de la ligne de la timezone
        config_content += 'timezone: Europe/Paris' + '\n'
    else:
        config_content += 'timezone: ' + conf['TIEMZONE'] + '\n'
    print('\t' + 'définition de la timezone ' + '.' * 39 + ' done')

    if conf['LANG'] == '':                                                                                  # génération de la ligne de la langue
        config_content += 'lang: fr_FR' + '\n'
    else:
        config_content += 'lang: ' + conf['LANG'] + '\n'
    print('\t' + 'définition de la langue ' + '.' * 41 + ' done')

    if conf['ADMIN_ZONE_URL'] == '':                                                                        # génération de la ligne de l'accès a la zone admin
        config_content += 'admin: admin/' + '\n'
    else:
        if conf['ADMIN_ZONE_URL'][strlen(conf['ADMIN_ZONE_URL']) - 1:strlen(conf['ADMIN_ZONE_URL'])] != '/':
            config_content += 'admin: ' + conf['ADMIN_ZONE_URL'] + '\n'
        else:
            config_content += 'admin: ' + conf['ADMIN_ZONE_URL'] + '\n'
    print('\t' + 'définition de la zone d\'administration ' + '.' * 27 + ' done')

    if conf['MODULES_FOLDER'] == '':                                                                        # génération de la ligne des modules
        config_content += 'mod_folder: modules' + '\n'
    else:
        os.rename(src_path + 'modules', src_path + conf['MODULES_FOLDER'])
        if os.path.isdir(src_path + conf['MODULES_FOLDER']):
            print(
                '\t' + 'renomage du dossier concernant les modules ' + '.' * 22 + ' done')
        config_content += 'mod_folder: ' + conf['MODULES_FOLDER'] + '\n'
    print('\t' + 'définition du dossier contenant les modules ' + '.' * 22 + ' done')

    if conf['FRONT_HOME'] == '':                                                                            # génération de la ligne du front
        config_content += 'front_home: home' + '\n'
    else:
        config_content += 'front_home: ' + conf['FRONT_HOME'] + '\n'
    print('\t' + 'définition du module d\'accueil des utilisateurs ' + '.' * 19 + ' done')

    if conf['ADMIN_HOME'] == '':                                                                            # génération de la ligne de l'admin
        config_content += 'admin_home: home' + '\n'
    else:
        config_content += 'admin_home: ' + conf['ADMIN_HOME'] + '\n'
    print('\t' + 'définition du module d\'accueil des utilisateurs ' + '.' * 19 + ' done')

    if conf['HOME_PAGE'] == '':                                                                             # génération de la ligne du controller par défault
        config_content += 'home_page: main' + '\n'
    else:
        config_content += 'home_page: ' + conf['HOME_PAGE'] + '\n'
    print('\t' + 'définition du controller par defaut ' + '.' * 31 + ' done')

    if conf['HOME_CLASS'] == '':                                                                            # génération de la ligne de la classe par défault
        config_content += 'home_class: main' + '\n'
    else:
        config_content += 'home_class: ' + conf['HOME_CLASS'] + '\n'
    print('\t' + 'définition de la class par defaut ' + '.' * 33 + ' done')

    if conf['DEFAULT_MEMCACHE_TIME'] == '':                                                                 # génération de la ligne de temps de défault du memcache
        config_content += 'memcache_time: 10' + '\n'
    else:
        config_content += 'memcache_time: ' + \
            conf['DEFAULT_MEMCACHE_TIME'] + '\n'
    print('\t' + 'définition du temps de memcache par defaut ' + '.' * 24 + ' done')

    """
    génération du bloc de blacklisting des modules
    """
    config_content += 'module_blacklist:' + '\n'
    if conf['MODULES_BLACKLIST'] != '':
        decoup = conf['MODULES_BLACKLIST'].split(',')
        index = 0
        while index < len(decoup):
            config_content += '- ' + decoup[index] + '\n'
            index = index + 1

    config_file = open(src_path + 'config.yaml', 'wb')                                                      # création du nouveau fichier config.yaml
    config_file.write(config_content)                                                                       # écriture du contenu du fichier config.yaml
    config_file.close()                                                                                     # fermeture du fichier config.yaml

    if os.path.isfile(src_path + 'config.yaml'):
        print('\t' + 'enregistrement du fichier config.yaml ' + '.' * 29 + ' done')
    else:
        print('\t' + 'enregistrement du fichier config.yaml ' + '.' * 29 + ' failed')
