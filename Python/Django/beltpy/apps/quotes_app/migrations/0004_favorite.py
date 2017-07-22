# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-21 22:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes_app', '0003_auto_20170721_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes_app.Quote')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes_app.User')),
            ],
        ),
    ]