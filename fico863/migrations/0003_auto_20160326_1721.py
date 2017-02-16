# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fico863', '0002_auto_20160326_1416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='REPORTTIME',
            new_name='REPORTDATE',
        ),
        migrations.AlterField(
            model_name='queryhistory',
            name='CREDITAUDIT',
            field=models.CharField(default=b'', max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='queryhistory',
            name='PAYMENT',
            field=models.CharField(default=b'', max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='queryhistory',
            name='TIMESTAMP',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
