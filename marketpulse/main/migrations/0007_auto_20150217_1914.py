# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_location_is_online'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
            preserve_default=True,
        ),
    ]
