# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('push_notifications', '0002_auto_20151208_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apnsdevice',
            name='user',
            field=models.ForeignKey(related_name='user_apn_devices', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='gcmdevice',
            name='user',
            field=models.ForeignKey(related_name='user_gcm_devices', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
