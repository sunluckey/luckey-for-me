# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-06 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='游戏名字')),
                ('type', models.CharField(max_length=255, verbose_name='游戏类型')),
                ('time', models.DateField(verbose_name='发表日期')),
                ('img', models.ImageField(default=None, null=True, upload_to='game_img')),
            ],
        ),
    ]
