# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-31 14:40
from __future__ import unicode_literals

import Accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(error_messages={'blank': 'First name must be provided.'}, max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(error_messages={'blank': 'Last name must be provided.'}, max_length=255, verbose_name='first name')),
                ('profile_pic', models.ImageField(upload_to=Accounts.models.user_directory_path)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
