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

from . import weather
from . import astro


def get_info(ip: str = 'auto_ip'):
    weather_info = weather.WeatherNow(ip=ip)
    astro_info = astro.Astronomy(
        city=weather_info.city,
        latitude=weather_info.latitude,
        longitude=weather_info.longitude
    )

    return weather_info, astro_info


def run(ip: str = ''):
    import beeprint
    w, a = get_info()
    beeprint.pp(w)
    beeprint.pp(a)
