"""NPUPA_workbench URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

app_name = 'downloader'
urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('upload/', views.upload, name='upload'),
    path('downloads/', views.downloads, name='downloads'),
    path('contents/', views.download_file, name='contents'),

    # url(r'^download/',views.download,name="download"),
]
