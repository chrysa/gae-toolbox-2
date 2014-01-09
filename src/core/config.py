#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import yaml


def get_config(target):
    f = open(os.getcwd() + os.sep + 'config.yaml', 'r')
    doc = yaml.load(f)

    return doc [target]    

ADMIN_PATH  = os.getcwd() + os.sep + get_config('mod_folder') + os.sep + 'admin'
CORE_PATH   = os.getcwd() + os.sep + 'core'
ERRORS_PATH = os.getcwd() + os.sep + get_config('mod_folder') + os.sep + 'errors'
FRONT_PATH  = os.getcwd() + os.sep + get_config('mod_folder') + os.sep + 'front'
LIBS_PATH   = os.getcwd() + os.sep + get_config('mod_folder') + os.sep + 'libs'
