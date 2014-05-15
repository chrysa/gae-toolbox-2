  # -*- coding= utf-8 -*-
  # disco-toolbox.src.core.controllers.config -- fichier de configuration générale du site
import os

NDD                    = 'appspot.com'      # définition du nom de domain de production
ENVOI_CONTACT          = ' '                # adresse d'expédition des e-mails
RECEPTION_CONTACT      = ' '                # adresse de réception des e-mails
SITE_TITLE             = 'disco GAE toolbox'# nom du site a afficher en title du site
TIMEZONE               = 'Europe/Paris'     # fuseau horaire par défault
LANG                   = 'fr_FR'            # langue du site par défault
FRONT_HOME             = 'home'             # nom du module d'accueil
ADMIN_HOME             = 'home'     
HOME_PAGE              = 'main'	            # nom de la page controllers appelé par défault lors du premier chargement du module
HOME_CLASS             = 'main'             # nom de la class appelé par défault lors du premier chargement d'une page
MODULES_FOLDER		   = 'modules'
MODULES_FRONT_FOLDER   = 'front'            # nom du dossier contenant les modules
MODULES_ADMIN_FOLDER   = 'admin'            # nom du dossier contenant les modules
ADMIN_ZONE_URL 		   = 'admin/'
MODULES_BLACKLIST      = []                 # liste des modules dont l'accès par URL est interdit
DEFAULT_MEMCACHE_TIME  = 10                 # durée de sauvegarde des données dans le datastore en seconde

PROJECT_PATH           = os.getcwd()         # chemin d'accès absolu au projet
ADMIN_PATH             = PROJECT_PATH + os.sep + MODULES_FOLDER + os.sep + MODULES_ADMIN_FOLDER + os.sep                   # chemin absolu d'accès aux modules
FRONT_PATH             = PROJECT_PATH + os.sep + MODULES_FOLDER + os.sep + MODULES_FRONT_FOLDER + os.sep                   # chemin absolu d'accès aux modules
CORE_PATH              = PROJECT_PATH + os.sep + 'core' + os.sep                                 # chemin absolu  d'accès au dossier core
DEBUG                  = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')                 # définition de l'état du débug suivant si on tourne sur le SDK ou le serveur de prod

# initialisation du domaine et de l'URl d'accès au site
if DEBUG:
    DOMAIN 			   = 'localhost'
    SITE_URL 		   = 'http://' + os.environ['SERVER_NAME'] + ':' + os.environ['SERVER_PORT']
else:
    DOMAIN 			   = '<instance:[\w]+>.<DOMAIN:[\w]+>.' + NDD
    SITE_URL 		   = 'http://' + os.environ['SERVER_NAME']
