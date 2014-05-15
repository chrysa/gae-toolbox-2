#!/usr/bin/env python
# -*- coding: utf-8 -*-

  # -*- coding: utf-8 -*-
  # disco-toolbox.src.core.controllers.date -- fichier de gestion des dates et des timestamps
import os
import time
from datetime import datetime

from pytz import timezone

from core import config                                                                                                      # import du fichier de config


def GetTimestamp(fuseau = config.TIMEZONE, date_format = 0):
    """fonction de récupération du timestamp actuel dans le fuseau horaire ciblé
    :param fuseau:      fuseau horaire ciblé  initialisé avec le fuseau horaire défini dans le fichier de config
    :param date_format: définit le retour soit sous forme de timestamp sous forme d'une date
    :returns:           date sous forme de timestamp ou de date formatée
    :rtype:             timestamp
    """
    timestamp      = datetime.now(timezone(fuseau))
    if date_format == 0:
        timestamp  = time.mktime(timestamp.timetuple())

    return timestamp


def GetDate(fuseau = config.TIMEZONE):
    """fonction de récupération de la date
    :param fuseau:      fuseau horaire ciblé  initialisé avec le fuseau horaire défini dans le fichier de config
    :returns:           retourne le jour le mois et l'année
    :rtype:             string
    """
    return GetTimestamp(fuseau, 1).strftime('%d/%m/%Y')


def GetHoraire(fuseau = config.TIMEZONE):
    """fonction de récupération de l'horaire
    :param fuseau:      fuseau horaire ciblé  initialisé avec le fuseau horaire défini dans le fichier de config
    :returns:           retourne l'heure les minutes et les secondes courantes
    :rtype:             string
    """
    return GetTimestamp(fuseau, 1).strftime('%H h %M min et %S s')


def GetYear(fuseau = config.TIMEZONE):
    """fonction de récupération de l'année
    :param fuseau:      fuseau horaire ciblé  initialisé avec le fuseau horaire défini dans le fichier de config
    :returns:           retourne l'heure les minutes et les secondes courantes
    :rtype:             number
    """
    return GetTimestamp(fuseau, 1).strftime('%Y')


def GetMonth(fuseau = config.TIMEZONE):
    """fonction de récupération du mois
    :param fuseau:      fuseau horaire ciblé  initialisé avec le fuseau horaire défini dans le fichier de config
    :returns:           retourne le numéro du mois en cours
    :rtype:             number
    """
    return GetTimestamp(fuseau, 1).strftime('%m')


def GetDay(fuseau = config.TIMEZONE):
    """fonction de récupération du jour
    :param fuseau:      fuseau horaire ciblé  initialisé avec le fuseau horaire défini dans le fichier de config
    :returns:           retourne la position menssuelle du jour en cours
    :rtype:             number
    """
    return GetTimestamp(fuseau, 1).strftime('%d')


def GetHour(fuseau = config.TIMEZONE):
    """fonction de récupération de l'heure
    :param fuseau:      fuseau horaire ciblé  initialisé avec le fuseau horaire défini dans le fichier de config
    :returns:           retourne l'heure à deux chiffres en cours
    :rtype:             number
    """
    return GetTimestamp(fuseau, 1).strftime('%H')


def GetMinute(fuseau = config.TIMEZONE):
    """fonction de récupération des minutes
    :param fuseau:      fuseau horaire ciblé  initialisé avec le fuseau horaire défini dans le fichier de config
    :returns:           retourne la minute à deux chiffres en cours
    :rtype:             number
    """
    return GetTimestamp(fuseau, 1).strftime('%M')


def GetSecond(fuseau = config.TIMEZONE):
    """fonction de récupération des secondes
    :param fuseau:      fuseau horaire ciblé  initialisé avec le fuseau horaire défini dans le fichier de config
    :returns:           retourne la seconde à deux chiffres en cours
    :rtype:             number
    """
    return GetTimestamp(fuseau, 1).strftime('%S')
