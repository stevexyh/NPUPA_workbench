#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
* Project Name : npupa_bot
* File Name    : weather.py
* Description  : Query weather forecast
* Create Time  : 2020-05-13 11:26:21
* Version      : 1.0
* Author       : Steve X
* GitHub       : https://github.com/Steve-Xyh
'''

import json
import requests

try:
    from functions import token as tk
except ModuleNotFoundError:
    import sys
    sys.path.append('../..')
    from functions import token as tk

wthr_key = tk.get_weather_key()


class Weather(object):
    weather_type = ''

    def get_coordinate(self):
        lat = str(self.latitude) + ' N' if self.latitude > 0 else ' S'
        lon = str(self.longitude) + ' E' if self.longitude > 0 else ' W'
        return (lat, lon)

    def request(self):
        url = f'https://free-api.heweather.net/s6/weather/{self.weather_type}?location={self.ip}&key={wthr_key}'
        self.res_json = requests.get(url).text
        self.res_dict = json.loads(self.res_json)['HeWeather6'][0]
        self.time_zone = 'UTC ' + self.res_dict['basic']['tz']
        self.update_time = self.res_dict['update']['loc']

        self.location = self.res_dict['basic']['location']
        self.city = self.res_dict['basic']['parent_city']
        self.admin_area = self.res_dict['basic']['admin_area']
        self.country = self.res_dict['basic']['cnty']
        self.latitude = float(self.res_dict['basic']['lat'])
        self.longitude = float(self.res_dict['basic']['lon'])
        self.lat_str, self.lon_str = self.get_coordinate()

    def __init__(self, ip: str = '', location: str = '北京', latitude: float = 40, longitude: float = 116):
        self.ip = ip
        self.update_time = ''
        self.time_zone = ''
        self.res_json = ''
        self.res_dict = {}

        self.location = location
        self.city = ''
        self.admin_area = ''
        self.country = ''
        self.latitude = latitude
        self.longitude = longitude
        self.lat_str, self.lon_str = self.get_coordinate()


class WeatherNow(Weather):
    weather_type = 'now'

    def request(self):
        Weather.request(self)
        aqi_url = f'https://free-api.heweather.net/s6/air/now?location={self.ip}&key={wthr_key}'
        self.aqi_json = requests.get(aqi_url).text
        self.aqi_dict = json.loads(self.aqi_json)['HeWeather6'][0]

    def __init__(self, ip: str = '', location: str = '北京', latitude: float = 39.90498734, longitude: float = 116.4052887):
        Weather.__init__(self, ip, location, latitude, longitude)
        self.aqi_json = ''
        self.aqi_dict = {}
        self.request()


def run():
    import beeprint

    x = WeatherNow(ip='auto_ip')
    x.request()
    print(x.weather_type)

    beeprint.pp(x.__dict__, indent=4)
