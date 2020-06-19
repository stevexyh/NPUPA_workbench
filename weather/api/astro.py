#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
---------------------------------------------
* Project Name : NPUPA_workbench
* File Name    : astro.py
* Description  : Query info for the Sun and Moon
* Create Time  : 2020-06-19 16:01:17
* Version      : 1.0
* Author       : Steve X
* GitHub       : https://github.com/Steve-Xyh
---------------------------------------------
* Notice
- Latitude & Longitude are required
---------------------------------------------
'''

import datetime
import astral
import pytz
from astral.sun import sun
from astral import LocationInfo


class Astronomy():
    def __init__(self, city: str = '', latitude: float = 0, longitude: float = 0):
        self.city = city
        self.latitude = latitude
        self.longitude = longitude


latitude = 46.582859
longitude = 125.138808

city = LocationInfo(latitude=latitude, longitude=longitude,
                    timezone='Asia/Shanghai')
print((
    f"Information for {city.name}/{city.region}\n"
    f"Timezone: {city.timezone}\n"
    f"Latitude: {city.latitude:.02f}; Longitude: {city.longitude:.02f}\n"
))


# obs = astral.Observer(latitude=latitude, longitude=longitude)
s = tk.get_confsun(city.observer, date=datetime.datetime.now(),
                   tzinfo=pytz.timezone('Asia/Shanghai'))

gd_r_begin, gd_r_end = tk.get_confgolden_hour(
    city.observer, direction=astral.SunDirection.RISING, tzinfo=pytz.timezone('Asia/Shanghai'))
gd_s_begin, gd_s_end = tk.get_confgolden_hour(
    city.observer, direction=astral.SunDirection.SETTING, tzinfo=pytz.timezone('Asia/Shanghai'))

print((
    f'Dawn:    {s["dawn"]}\n'
    f'Sunrise: {s["sunrise"]}\n'
    f'Noon:    {s["noon"]}\n'
    f'Sunset:  {s["sunset"]}\n'
    f'Dusk:    {s["dusk"]}\n'

    f'Golden Hour Rise:    {str(gd_r_begin), str(gd_r_end)}\n'
    f'Golden Hour Set:    {str(gd_s_begin), str(gd_s_end)}\n'
    # f'Blue Hour:    {s["dusk"]}\n'
))

print(astral.SunDirection.RISING)
print(astral.SunDirection.SETTING)