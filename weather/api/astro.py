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


class Astronomy(object):

    def init_location(self, timezone: str = 'Asia/Shanghai'):
        location = LocationInfo(
            latitude=self.latitude,
            longitude=self.longitude,
            timezone=timezone
        )

        return location

    def init_sun(self):
        sun_info = astral.sun.sun(
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

    def __init__(self, city: str = '', latitude: float = 0, longitude: float = 0):
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.location = self.init_location()
        self.sun = self.init_sun()


if __name__ == "__main__":
    import beeprint

    try:
        from functions import format_string as fs
    except ModuleNotFoundError:
        import sys
        sys.path.append('../..')
        from functions import format_string as fs

    latitude = 40
    longitude = 120

    astro = Astronomy(latitude=latitude, longitude=longitude)
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
