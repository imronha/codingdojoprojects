# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-19 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
