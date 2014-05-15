  # -*- coding: utf-8 -*-
  # disco-toolbox.src.core.controllers.memC -- fichier d'interaction avec le datastore intégrant le memcache
import logging
from google.appengine.ext import db
from google.appengine.api import memcache

from core                 import config                                                                                 # appel du fichier de configuration globale de l'application


def get_datas_to_ds(request, nbr_return=1, offset=0):
    """fonction de récupération des données depuis le datastore
    :param request:    requête de selection a excuter
    :param nbr_return: nombre de résultats a retourner
    :param offset:     décalage pour commencer a récupérer les données
    :returns:          dictionnaire de données
    """
    if nbr_return == '1':
        results = db.GqlQuery(request)                                                                                  # récupération d'un résultat unique
    else:
        results = db.GqlQuery(request).fetch(nbr_return, offset)                                                        # récupération d'une tranche de résultats

    return results                                                                                                      # retour du résultat de la sélection


def get_datas_to_mem(key, request, nbr_return, offset, time=config.DEFAULT_MEMCACHE_TIME):
    """fonction de récupération et d'ajout de données dans le memcache
    :param key:  kind des données a récupérer
    :param request:    requête de selection a excuter
    :param nbr_return: ombre de résultats a retourner
    :param offset:     décalage pour commencer a récupérer les données
    :param time:      durée de sauvegarde des données dans le memcache par défaut 10 secondes
    :returns:          dictionnaire de données
    """
    datas = memcache.get(key)                                                                                           # récupération des valeurs cibles dans le memcache
    if datas is None:                                                                                                   # test d'existence des données récupérés
        datas = get_data_to_ds(request, nbr_return, offset)                                                             # récupération des données dans le datas store si elle n'existe pas dans le memcache
        if not add_datas(key, datas, time):                                                                             # test du résultat de l'ajout des données dans le memcahce
            logging.error('get '+str(key)+' to memcache failed.')                                                       # si l'ajout n'as pas fonctionné on lève une erreur

    return datas                                                                                                        # renvoi des données se trouvant dans le memcache


def add_datas_to_mem(key, datas, time=config.DEFAULT_MEMCACHE_TIME):
    """fonction de définition de la valeur d'une clé dans le memcache seulement si elle n'est pas présente précédement
    :param request:    requête de selection a excuter
    :param nbr_return: nombre de résultats a retourner
    :param offset:     décalage pour commencer a récupérer les données
    """
    if not memcache.add(key, datas, time):
        logging.error('add ' + str(key) + ' to memcache failed.')                                                       # ajout de la valeur dans le memcache


def set_datas_to_mem(key, value, time=config.DEFAULT_MEMCACHE_TIME):
    """fonction de définition de la valeur d'une clé dans le memcache quelque soit la valeur précédente
    :param key:        clé à définir
    :param value:      valeur à définir
    :param time:       durée avant expiration en secondes
    """
    if not memcache.set(key, value, time):
        logging.error('set ' + str(key) + ' to memcache failed.')                                                       # initialisation de la valeur dans le memcache


def replace_datas_to_mem(key, value, time=config.DEFAULT_MEMCACHE_TIME):
    """fonction de remplacement de la valeur d'une clé dans le memcache
    :param key:        clé cible
    :param value:      nouvelle valeur de la clé
    :param time:       durée avant expiration
    """
    if not memcache.replace(key, value, time):
        logging.error('replace of ' + str(key) + ' to memcache failed.')                                                # remplacement de la valeur dans le memcache


def delete_datas_to_mem(key, seconds=0):
    """fonction de  suppression d'une clé du memcache
    :param key:        clé à supprimer
    :param seconds :   durée facultative en secondes pendant laquelle les objets supprimés sont verrouillés
    """
    if not memcache.delete(key, seconds):
        logging.error('delete ' + str(key) + ' to memcache failed.')                                                    # suppression de la valeur dans le memcache
