# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-21 22:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes_app', '0002_quote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='fav_quote',
            new_name='quote_by',
        ),
    ]