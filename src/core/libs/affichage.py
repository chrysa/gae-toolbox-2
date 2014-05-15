#!/usr/bin/env python
# -*- coding: utf-8 -*-

  # -*- coding: utf-8 -*-
  # disco-toolbox.src.core.controllers.affichage -- fichier de gestion de l'affichage
import os
from google.appengine.ext.webapp import template

from core.libs                   import date                                                                       # import du fichier de gestion des dates
from core                        import config                                                                     # import du fichier de configuration globale

VIEW_CORE_PATH = config.CORE_PATH + 'views'                                                                        # chemin d'accès aux dossier des vues du core


def code_render(page, value):
    """fonction de renvoi du code source de la page a afficher
    :param page:   le nom de la page
    :param value:  les values de la page a afficher
    :returns:      la structure de la page générée
    :rtype:        string
    """
    return template.render(page, value)

def render(objet, page, value):
    """fonction d'affichage du template sélectionné
    :param objet:  l'objet en cours de traitement
    :param page:   nom de la page
    :param value: les value de la page a afficher
    :returns:      affiche la page généré
    :rtype:        string
    """
    objet.out.write(code_render(page, value))

def GetView(name, module='', admin='0'):
    """fonction d'appel d'une vue HTML stockée a la racine du dossier des vues du module
    :param name:   nom de la vue
    :param module: nom du module contenant
    :returns:      le chemin complet de la vue
    :rtype:        string
    """
    if module == '':
        return VIEW_CORE_PATH + os.sep + 'errors' + os.sep + name + '.html'
    else:
        if admin == '1':
            return config.MODULES_PATH + config.MODULES_ADMIN_FOLDER + os.sep + module + os.sep + 'views' + os.sep + name + '.html'
        else:
            return config.MODULES_PATH + config.MODULES_FRONT_FOLDER + os.sep + module + os.sep + 'views' + os.sep + name + '.html'

def GetStaticView(name, module='', admin='0'):
    """fonction d'appel d'une vue HTML stockée dans le dossier des vues statics du module
    :param name:   nom de la vue
    :param module: nom du module contenant
    :returns:      le chemin complet de la vue
    :rtype:        string
    """
    if module == '':
        return VIEW_CORE_PATH + os.sep + 'static' + os.sep + name + '.html'
    else:
        if admin == '1':
            return config.MODULES_PATH + config.MODULES_ADMIN_FOLDER + os.sep + module + os.sep + 'static' + os.sep + name + '.html'
        else:
            return config.MODULES_PATH + config.MODULES_FRONT_FOLDER + os.sep + module + os.sep + 'static' + os.sep + name + '.html'

def GetAjaxView(name, module='', admin='0'):
    """fonction d'appel d'une vue HTML stockée dans le dossier des vues issues de requêtes AJAX du module
    :param name:   nom de la vue
    :param module: nom du module contenant
    :returns:      le chemin complet de la vue
    :rtype:        string
    """
    if module == '':
        return VIEW_CORE_PATH + os.sep + 'ajax' + os.sep + name + '.html'
    else:
        if admin == '1':
            return config.MODULES_PATH + config.MODULES_ADMIN_FOLDER + os.sep + module + os.sep + 'ajax' + os.sep + name + '.html'
        else:
            return config.MODULES_PATH + config.MODULES_FRONT_FOLDER + os.sep + module + os.sep + 'ajax' + os.sep + name + '.html'

def GetErrorView(name, module='', admin='0'):
    """fonction d'appel d'une vue HTML représentant les erreurs générées par le site
    :param name:   nom de la vue
    :param module: nom du module contenant la vue par défault vide qui appel les erreurs de core/views/errors
    :returns:      le chemin complet de la vue
    :rtype:        string
    """
    if module == '':
        return VIEW_CORE_PATH + os.sep + 'errors' + os.sep + name + '.html'
    else:
        if admin == '1':
            return config.MODULES_PATH + config.MODULES_ADMIN_FOLDER + os.sep + module + os.sep + 'errors' + os.sep + name + '.html'
        else:
            return config.MODULES_PATH + config.MODULES_FRONT_FOLDER + os.sep + module + os.sep + 'errors' + os.sep + name + '.html'

def extend_to_base(objet, value):
    """fonction d'appel d'appel du template de base
    :param objet:
    :param value:
    :returns: le chemin complet de la vue
    :rtype:   string
    """
    if not 'head' in value:
        value['head']=code_render(GetStaticView('title'), {'title':config.SITE_TITLE})

    value['year']=date.GetYear()
    render(objet, GetStaticView('base'), value)
