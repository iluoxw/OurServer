# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('delete_flag', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='GroupPrivileges',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupId', models.IntegerField()),
                ('privilegesId', models.IntegerField()),
                ('delete_flag', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Privileges',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('delete_flag', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('delete_flag', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userId', models.IntegerField()),
                ('groupId', models.IntegerField()),
                ('delete_flag', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='UserPrivileges',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userId', models.IntegerField()),
                ('privilegesId', models.IntegerField()),
                ('delete_flag', models.CharField(max_length=4)),
            ],
        ),
    ]
