# -*- coding: utf-8 -*-

import config
import os

print('----| lancement du serveur appengine |----')
os.system('cd ' + config.APPENGINE +' && python dev_appserver.py ' + config.PROJECT_SRC + os.sep + 'app.yaml')