# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fico863', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='queryhistory',
            old_name='PERSONID',
            new_name='CERTIFICATECODE',
        ),
        migrations.AddField(
            model_name='queryhistory',
            name='SCOREDETAIL',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='queryhistory',
            name='SCORE',
            field=models.FloatField(null=True),
        ),
    ]
