# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-29 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='LinkedIn'),
        ),
        migrations.AddField(
            model_name='profile',
            name='mastodon',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Mastodon'),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Twitter'),
        ),
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Website'),
        ),
    ]
