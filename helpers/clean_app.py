#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil

if os.getcwd()[0:len(os.getcwd())-8] == 'helpers':
	target = os.getcwd()[0:len(os.getcwd())-8]
else:
	target = os.getcwd()[0:len(os.getcwd())]


print('----| nettoyage de l\'application |----')


def clean_file(target):
    for elt in os.listdir(target):
        if os.path.isdir(target + os.sep + elt):
            clean_file(target + os.sep + elt)
        else:
            if os.path.isfile(target + os.sep + elt) and elt[len(elt) - 4:len(elt)] == '.pyc':
                print('suppression de : ' + str(target + os.sep + elt))
                os.remove(target + os.sep + elt)

for elt in os.listdir(target):
    if os.path.isdir(target + os.sep + elt):
        print('nettoyage de ' + str(target + os.sep + elt) + ' ' + '.' * 20 + ' please wait')
        clean_file(target + os.sep + elt)
        print('nettoyage de ' + str(target + os.sep + elt) + ' ' + '.' * 20 + ' done')
