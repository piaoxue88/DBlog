# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-03-20 18:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('permission_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='users',
            field=models.ManyToManyField(related_name='roles', to=settings.AUTH_USER_MODEL),
        ),
    ]