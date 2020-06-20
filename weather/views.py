#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
---------------------------------------------
* Project Name : NPUPA_workbench
* File Name    : views.py
* Description  : Django views
* Create Time  : 2020-06-20 16:12:20
* Version      : 1.0
* Author       : Steve X
* GitHub       : https://github.com/Steve-Xyh
---------------------------------------------
'''


from django.shortcuts import render

# Create your views here.


def base(request):
    '''Render base template'''

    return render(request, 'weather/base.html')


def home(request):
    '''Render home page'''

    return render(request, 'weather/home.html')
