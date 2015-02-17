# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150217_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='is_online',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
