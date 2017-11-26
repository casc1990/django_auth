# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-11-26 08:33
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171126_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, error_messages={'required': '联系电话不能为空'}, help_text='包含11位数字的，不能以0开头', max_length=30, validators=[django.core.validators.RegexValidator(code='号码错误', message='请输入正确的电话或手机号码', regex='^[^0]\\d{6,7}$|^[1]\\d{10}$')], verbose_name='联系电话'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': '用户名不能重复'}, help_text='必填.150个字符或者更少.', max_length=150, unique=True),
        ),
    ]