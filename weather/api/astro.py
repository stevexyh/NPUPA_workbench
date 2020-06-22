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
from astral import LocationInfo
from astral.sun import sun
from astral import moon


class Astronomy(object):
    '''Class of astronomy info, including Sun & Moon'''

    def init_location(self, timezone: str = 'Asia/Shanghai'):
        '''Init LocationInfo object'''

        location = LocationInfo(
            latitude=self.latitude,
            longitude=self.longitude,
            timezone=timezone
        )

        return location

    def init_sun(self):
        '''Init Sun object'''

        sun_info = sun(
            self.location.observer,
            date=datetime.datetime.now(),
            tzinfo=pytz.timezone('Asia/Shanghai')
        )

        sun_info['golden_rise'] = astral.sun.golden_hour(
            self.location.observer,
            direction=astral.SunDirection.RISING,
            tzinfo=pytz.timezone('Asia/Shanghai')
        )

        sun_info['golden_set'] = astral.sun.golden_hour(
            self.location.observer,
            direction=astral.SunDirection.SETTING,
            tzinfo=pytz.timezone('Asia/Shanghai')
        )

        sun_info['blue_rise'] = astral.sun.blue_hour(
            self.location.observer,
            direction=astral.SunDirection.RISING,
            tzinfo=pytz.timezone('Asia/Shanghai')
        )

        sun_info['blue_set'] = astral.sun.blue_hour(
            self.location.observer,
            direction=astral.SunDirection.SETTING,
            tzinfo=pytz.timezone('Asia/Shanghai')
        )

        return sun_info

    def init_moon(self):
        '''Init Moon object'''

        moon_info = {}
        moon_info['phase'] = moon.phase()
        moon_info['percent'] = int((moon_info['phase'] if moon_info['phase'] <= 14 else (28 - moon_info['phase'])) / 14 * 100)

        if moon_info['phase'] < 7:
            moon_info['type'] = '新月'
            moon_info['icon'] = '10'
        elif moon_info['phase'] < 14:
            moon_info['type'] = '上弦月'
            moon_info['icon'] = '25'
        elif moon_info['phase'] < 21:
            moon_info['type'] = '满月'
            moon_info['icon'] = '100'
        else:
            moon_info['type'] = '下弦月'
            moon_info['icon'] = '75'

        return moon_info

    def __init__(self, city: str = '', latitude: float = 0, longitude: float = 0):
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.location = self.init_location()
        self.sun = self.init_sun()
        self.moon = self.init_moon()


if __name__ == "__main__":
    import beeprint

    astro = Astronomy(latitude=40, longitude=120)
    beeprint.pp(astro.__dict__, indent=4)

    print((
        f"Information for {astro.location.name}/{astro.location.region}\n"
        f"Timezone: {astro.location.timezone}\n"
        f"Latitude: {astro.location.latitude:.02f}; Longitude: {astro.location.longitude:.02f}\n"
    ))

    print((
        f'Dawn:    {astro.sun["dawn"]}\n'
        f'Sunrise: {astro.sun["sunrise"]}\n'
        f'Noon:    {astro.sun["noon"]}\n'
        f'Sunset:  {astro.sun["sunset"]}\n'
        f'Dusk:    {astro.sun["dusk"]}\n'

        f'Golden Rise:    {str(astro.sun["golden_rise"][0]), str(astro.sun["golden_rise"][1])}\n'
        f'Golden Set:    {str(astro.sun["golden_set"][0]), str(astro.sun["golden_set"][1])}\n'
        f'Blue Rise:    {str(astro.sun["blue_rise"][0]), str(astro.sun["blue_rise"][1])}\n'
        f'Blue Set:    {str(astro.sun["blue_set"][0]), str(astro.sun["blue_set"][1])}\n'
    ))
