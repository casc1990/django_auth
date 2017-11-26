# -*- coding:utf-8 -*-
from django.contrib import admin
from . models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    empty_value_display = u'空值'
    fields = ['username','password','email','is_active','mobile','nickname']
    search_fields = ['username']
    list_display = ['username','email','is_active','mobile','date_joined']
    ordering = ['date_joined']

admin.site.register(User,UserAdmin)
