# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150217_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='country_code',
        ),
        migrations.AlterField(
            model_name='location',
            name='address',
            field=models.CharField(default=b'', max_length=120, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
            preserve_default=True,
        ),
    ]
