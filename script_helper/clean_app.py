#!/usr/bin/env python
# -*- coding: utf-8 -*-

#! /usr/bin/python
# -*- coding: utf-8 -*-
import os
import config

print('----| nettoyage de l\'application |----')

def clean_file(target):
	for elt in os.listdir(target):
	  if os.path.isdir(target + os.sep + elt):
	  	clean_file(target + os.sep + elt)
	  else:
	  	if os.path.isfile(target + os.sep + elt) and elt[len(elt) - 4:len(elt)] == '.pyc':
	  		print('suppression de : ' + str(target + os.sep + elt))
			os.system('rm ' + target + os.sep + elt)

print('----------| nettoyage de l\'application '+ str(config.PROJECT_SRC) + ' |----------')
clean_file(config.PROJECT_SRC)
print('----------| nettoyage des scripts d\'help '+ str(config.PROJECT_HELP) + '  |----------')
clean_file(config.PROJECT_HELP)