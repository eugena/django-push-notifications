# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('push_notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gcmdevice',
            name='registration_id',
            field=models.CharField(max_length=512, verbose_name='Registration ID'),
        ),
    ]
