#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
---------------------------------------------
* Project Name : NPUPA_workbench
* File Name    : get_info.py
* Description  : Get info for weather and astronomy
* Create Time  : 2020-06-20 11:23:44
* Version      : 1.0
* Author       : Steve X
* GitHub       : https://github.com/Steve-Xyh
---------------------------------------------
* Notice
- Requires location info from weather.py
---------------------------------------------
'''

import beeprint
from . import weather
from . import astro


def get_info(ip_addr: str = 'auto_ip') -> list:
    '''
    Get weather & astro info

    Parameters::
        ip_addr - IP address for query location
    Returns::
        res: list - the query result
            - res[0] for weather_info
            - res[1] for astro_info
    '''

    weather_info = weather.WeatherNow(ip_addr=ip_addr)
    astro_info = astro.Astronomy(
        city=weather_info.city,
        latitude=weather_info.latitude,
        longitude=weather_info.longitude
    )

    res = [weather_info.__dict__, astro_info.__dict__]

    return res


def run(ip_addr: str = 'auto_ip'):
    '''Run test'''

    res = get_info(ip_addr=ip_addr)
    beeprint.pp(res)
