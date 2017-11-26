#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:pengbo

from django.conf.urls import url

from . import views


app_name = 'users'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
]