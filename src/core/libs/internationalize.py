  # -*- coding: utf-8 -*-
  # disco-toolbox.src.core.controllers.internationalize -- fichier de gestion du multilingue
import webapp2
from webapp2_extras import i18n

from core import config                                                                 # import du fichier de config


def set_config(config):
    """fonction d'intialisation de la configuration du multilingue
    :param config: disctionnaire de gestion de  la configuration
    :returns:      sous-dictionnaire pour la configuration des chemins de traduction
    :rtype:        dictionnaire
    """
    config['webapp2_extras.i18n'] = {'translations_path': ''}                           # initialisation de la route de traduction
    return config


def trad_conf(path, req):
    """fonction de la configuration du multilingue suivant le module
    :param path:   chemin d'accès relatif au dossier locale de la racine du site
    :param req:    requête reçu pour l'affichage
    :returns:      la configuration pour la récupération des traductions
    :rtype:        string
    """
    app                       = webapp2.get_app()                                       # récupération de la configuration de l'application définit dans le main
    trad                      = app.config.get('webapp2_extras.i18n')                   # récupération du sous-dictionnaire des langues
    trad['translations_path'] = path                                                    # définition du chemin des traduction
    locale                    = req.GET.get('locale', config.LANG)                      # récupération de la langue a choisir

    return i18n.get_i18n().set_locale(locale)                                           # retour de la configuraion des traductions


def trad(target):
    """fonction de récupération de la traduction d'une chaine de caractère
    :param target: code à traduire
    :returns:      traduction voulue
    :rtype:        string
    """
    return i18n.gettext(target)
