# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-26 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_upload', models.FileField(upload_to=b'')),
            ],
        ),
    ]
