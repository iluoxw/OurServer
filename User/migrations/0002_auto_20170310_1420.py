# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='name',
            new_name='group_name',
        ),
        migrations.RenameField(
            model_name='privileges',
            old_name='name',
            new_name='pri_name',
        ),
    ]
