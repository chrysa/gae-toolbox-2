#! /usr/bin/python
# -*- coding: utf-8 -*-
import os
import config

print('----| gestion du multilingue |----')


os.system('sudo chmod 700 -R ' + config.PROJECT_SRC)

continu       = True

while continu == True:
    choice    = ''
    if choice == '':
        aff = '------------------------------------------\n'
        aff += 'actions\n'
        aff += '------------------------------------------\n'
        aff += '1 => liste des langues prises en charge\n'
        aff += '2 => créer une nouvelle traduction\n'
        aff += '3 => compiler les traductions de l\'application\n'
        aff += '------------------------------------------'
        print(aff)
        choice = input('numéro de l\'action ? ')

    if choice   == 1:
        print('liste des codes langues ...')
        for elt in os.listdir(config.PROJECT_SRC + os.sep + 'core' + os.sep + 'locale'):
            print('\t' + str(elt))
    elif choice == 2:
        print('------------------------------------------')
        print('type de traduction a créer')
        print('------------------------------------------')
        print('1 => admin')
        print('2 => front')
        print('------------------------------------------')
        module_type = raw_input('type de module a créer ? ')
        if module_type == '1':
            print('plop')
            path_folder = config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.ADMIN_FOLDER
        else:
            print('ploup')
            path_folder = config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.FRONT_FOLDER
        print(path_folder)
        code = raw_input('code langue a créer ? ')
        """gestion des traductions du core"""
        print('traduction dans le core')
        print('\t' + 'création du dossier ...')
        os.system('cd ' + config.PROJECT_SRC + os.sep + 'core' + os.sep + 'locale && mkdir ' + code + ' && cd ' + code + ' && mkdir LC_MESSAGES')
        print('\t' + 'duplication des fichiers de tradtuction ...')
        for elt in os.listdir(config.PROJECT_SRC + os.sep + 'core' + os.sep + 'locale' + os.sep + config.LANG + os.sep + 'LC_MESSAGES'):
            ext = os.path.splitext(elt)
            if ext[1] == '.po':
                source = config.PROJECT_SRC + os.sep + 'core' + os.sep + 'locale' + os.sep + config.LANG + os.sep + 'LC_MESSAGES' + os.sep + elt
                target = config.PROJECT_SRC + os.sep + 'core' + os.sep + 'locale' + os.sep + code + os.sep + 'LC_MESSAGES' + os.sep + elt
                os.system('cp ' + source + ' ' + target)
                if os.path.isfile(target):
                    print('\t' + '\t''\t' + '\t' + 'le fichier ' + str(elt) + ' as bien été copié')
                else:
                    print('\t' + '\t' + 'le fichier ' + str(elt) + ' n\'as pas pu être copié')
        """gestion des traductions des modules"""
        print('gestion des traductions des modules')
        for elt in os.listdir(path_folder):
            print(elt)
            if os.path.isdir(path_folder + os.sep + elt):
                print('\t' + 'gestion des traductions du module ' + str(elt) + ' ...')
                print('\t' + '\t' + 'création du dossier ...')
                os.system('cd ' + path_folder + os.sep + elt + os.sep + 'locale && mkdir ' + code + ' && cd ' + code + ' && mkdir LC_MESSAGES')
                print('\t' + '\t' + 'duplication des fichiers de tradtuction ...')
                for sub_elt in os.listdir(path_folder + os.sep + elt + os.sep + 'locale' + os.sep + config.LANG + os.sep + 'LC_MESSAGES'):
                    ext = os.path.splitext(sub_elt)
                    if ext[1] == '.po':
                        source = path_folder + os.sep + elt + os.sep + 'locale' + os.sep + config.LANG + os.sep + 'LC_MESSAGES' + os.sep + sub_elt
                        target = path_folder + os.sep + elt + os.sep + 'locale' + os.sep + code + os.sep + 'LC_MESSAGES' + os.sep + sub_elt
                        os.system('cp ' + source + ' ' + target)
                        if os.path.isfile(target):
                            print('\t' + '\t' + '\t' + 'le fichier ' + str(sub_elt) + ' as bien été copié')
                        else:
                            print('\t' + '\t' + '\t' + 'le fichier ' + str(sub_elt) + ' n\'as pas pu être copié')
    elif choice == 3:
        # scan du locale du core
        print('purge du core')
        for elt in os.listdir(config.PROJECT_SRC + os.sep + 'core' + os.sep + 'locale'):
            # parcour des langues
            print('\t' + 'purge des compilations de la langue ' + str(elt))
            for sub_elt in os.listdir(config.PROJECT_SRC + os.sep + 'core' + os.sep + 'locale' + os.sep + elt + os.sep + 'LC_MESSAGES'):
                # suppression des .mo dans chaques langues
                ext = os.path.splitext(sub_elt)
                if ext[1] == '.mo':
                    os.system('rm ' + config.PROJECT_SRC + os.sep + 'core' + os.sep + 'locale' + os.sep + elt + os.sep + 'LC_MESSAGES' + os.sep + sub_elt)
                    print('\t' + '\t' + 'suppression de ' + str(sub_elt))
                name = sub_elt[0:len(sub_elt) - 3]
                # compilation des nouveaux .mo
                os.system('cd ' + config.PROJECT_SRC + os.sep + 'core' + os.sep + 'locale' + os.sep + elt + os.sep + 'LC_MESSAGES' + os.sep + ' && msgfmt -o ' + name + '.mo -v ' + name + '.po')
        # scan des front modules
        print('purge des front modules')
        for mod in os.listdir(config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.FRONT_FOLDER):
            # parcour du module en cour
            if os.path.isdir(config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.FRONT_FOLDER + os.sep + mod):
                print('\t' + 'purge du module ' + str(mod))
                for lang in os.listdir(config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.FRONT_FOLDER + os.sep + mod + os.sep + 'locale'):
                    # parcour des langues
                    print('\t' + '\t' + 'purge des compilations de la langue ' + str(lang))
                    for elt in os.listdir(config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.FRONT_FOLDER + os.sep + mod + os.sep + 'locale' + os.sep + lang + os.sep + 'LC_MESSAGES'):
                        # suppression des .mo dans chaques langues
                        ext = os.path.splitext(elt)
                        if ext[1] == '.mo':
                            os.system('rm ' + config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.FRONT_FOLDER + os.sep + mod + os.sep + 'locale' + os.sep + lang + os.sep + 'LC_MESSAGES' + os.sep + elt)
                            print('\t' + '\t' + '\t' + 'suppression de ' + str(elt))
                        name = elt[0:len(elt) - 3]
                        # compilation des nouveaux .mo
                        os.system('cd ' + config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.FRONT_FOLDER + os.sep + mod + os.sep + 'locale' + os.sep + 'LC_MESSAGES' + os.sep + lang + ' && msgfmt -o ' + name + '.mo -v ' + name + '.po')
        # scan des admins modules
        print('purge des admins modules')
        for mod in os.listdir(config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.ADMIN_FOLDER):
            # parcour du module en cour
            if os.path.isdir(config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.ADMIN_FOLDER + os.sep + mod):
                print('\t' + 'purge du module ' + str(mod))
                for lang in os.listdir(config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.ADMIN_FOLDER + os.sep + mod + os.sep + 'locale'):
                    # parcour des langues
                    print('\t' + '\t' + 'purge des compilations de la langue ' + str(lang))
                    for elt in os.listdir(config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.ADMIN_FOLDER + os.sep + mod + os.sep + 'locale' + os.sep + lang + os.sep + 'LC_MESSAGES'):
                        # suppression des .mo dans chaques langues
                        ext = os.path.splitext(elt)
                        if ext[1] == '.mo':
                            os.system('rm ' + config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.ADMIN_FOLDER + os.sep + mod + os.sep + 'locale' + os.sep + lang + os.sep + 'LC_MESSAGES' + os.sep + elt)
                            print('\t' + '\t' + '\t' + 'suppression de ' + str(elt))
                        name = elt[0:len(elt) - 3]
                        # compilation des nouveaux .mo
                        os.system('cd ' + config.PROJECT_SRC + os.sep + config.MODULES_FOLDER + os.sep + config.ADMIN_FOLDER + os.sep + mod + os.sep + 'locale' + os.sep + 'LC_MESSAGES' + os.sep + lang + ' && msgfmt -o ' + name + '.mo -v ' + name + '.po')
    c = raw_input('effectuer une autre action [Y] ou quitter [N] ? [Y/N] ')
    if c == 'N' or c == 'n':
        continu = False
    else:
        continu = True

