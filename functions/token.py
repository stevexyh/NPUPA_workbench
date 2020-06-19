#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
* File Name    : token.py
* Description  : Get token from files
* Create Time  : 2020-03-13 12:18:29
* Version      : 1.0
* Author       : Steve X
* GitHub       : https://github.com/Steve-Xyh
'''


import configparser


TOKEN_FILE = '.sec_key'
INIT_CONF = '.init.conf'

conf = configparser.ConfigParser()
conf.read(INIT_CONF)


def get_token():
    '''Get token from files'''
    token = ''
    with open(TOKEN_FILE, 'r') as f:
        token = f.readline().strip()

    return token


def get_weather_key():
    '''Get weather api key from files'''
    token = conf.get('weather', 'key')

    return token


def get_conf(section: str = '', option: str = ''):
    '''Get config from files'''
    res = conf.get(section=section, option=option)

    return res
