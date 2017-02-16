# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fico863', '0003_auto_20160326_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='overdraftoverdue',
            name='REPORTDATE',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
