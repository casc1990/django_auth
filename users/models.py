# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, Group, Permission, PermissionsMixin


class UserGroup(Group):
    group_name = models.CharField(max_length=80, unique=True, verbose_name=u'用户组')
    comment = models.TextField(blank=True, null=True, verbose_name=u'备注')

    def clean(self):
        self.name = self.group_name

    def __str__(self):
        return self.group_name

    class Meta:
        #default_permissions = ()
        verbose_name = u'用户组'
        verbose_name_plural = u'用户组管理'

class User(AbstractUser):
    USER_ROLE_CHOICES = (
        ('SU', u'超级管理员'),
        ('GA', u'组管理员'),
        ('CU', u'普通用户')
    )
    #username = models.CharField(max_length=150,unique=True,help_text=u'必填.150个字符或者更少.',
    #                            verbose_name=u'用户名',error_messages={'unique':u'用户名不能重复'})
    nickname = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=30, blank=True, verbose_name=u'联系电话', validators=[
        RegexValidator(regex='^[^0]\d{6,7}$|^[1]\d{10}$', message=u'请输入正确的电话或手机号码', code=u'号码错误')],
                              error_messages={'required': u'联系电话不能为空'},
                              help_text=u'包含11位数字的，不能以0开头')
    position = models.CharField(max_length=20, blank=True, verbose_name=u'职位')
    role = models.CharField(max_length=2, choices=USER_ROLE_CHOICES, default='CU')
    group = models.ManyToManyField(UserGroup, related_name='user_group_set', verbose_name=u'用户属组')

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        #default_permissions = ()
        #permissions = (
        #    ('view_user', u'查看用户'),
        #   ('edit_user', u'管理用户'),
        #)
        verbose_name = u'用户'
        verbose_name_plural = u'用户管理'


