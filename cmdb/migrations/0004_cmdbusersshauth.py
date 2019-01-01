# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-16 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_cmdbansiblesshinfo_cmdbproductinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CmdbUserSshAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('user_key', models.TextField(blank=True, null=True)),
                ('related_node', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=32, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, db_column='Create_Time', null=True)),
                ('update_time', models.DateTimeField(auto_now=True, db_column='Update_Time', null=True)),
                ('special_ip', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cmdb_user_ssh_auth',
            },
        ),
    ]
