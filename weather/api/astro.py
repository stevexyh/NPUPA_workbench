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


class Astronomy(object):

    def __init__(self, city: str = '', latitude: float = 0, longitude: float = 0):
        self.city = city
        self.latitude = latitude
        self.longitude = longitude


latitude = 46.582859
longitude = 125.138808

location = LocationInfo(
    latitude=latitude,
    longitude=longitude,
    timezone='Asia/Shanghai'
)

print((
    f"Information for {location.name}/{location.region}\n"
    f"Timezone: {location.timezone}\n"
    f"Latitude: {location.latitude:.02f}; Longitude: {location.longitude:.02f}\n"
))


# obs = astral.Observer(latitude=latitude, longitude=longitude)
sun_info = astral.sun.sun(
    location.observer,
    date=datetime.datetime.now(),
    tzinfo=pytz.timezone('Asia/Shanghai')
)

gd_r_begin, gd_r_end = astral.sun.golden_hour(
    location.observer,
    direction=astral.SunDirection.RISING,
    tzinfo=pytz.timezone('Asia/Shanghai')
)
gd_s_begin, gd_s_end = astral.sun.golden_hour(
    location.observer,
    direction=astral.SunDirection.SETTING,
    tzinfo=pytz.timezone('Asia/Shanghai')
)

print((
    f'Dawn:    {sun_info["dawn"]}\n'
    f'Sunrise: {sun_info["sunrise"]}\n'
    f'Noon:    {sun_info["noon"]}\n'
    f'Sunset:  {sun_info["sunset"]}\n'
    f'Dusk:    {sun_info["dusk"]}\n'

    f'Golden Hour Rise:    {str(gd_r_begin), str(gd_r_end)}\n'
    f'Golden Hour Set:    {str(gd_s_begin), str(gd_s_end)}\n'
    f'Blue Hour:    {sun_info["dusk"]}\n'
))

print(sun_info)

if __name__ == "__main__":

    pass
