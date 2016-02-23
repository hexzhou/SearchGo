# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mall', '0003_auto_20151213_0905'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pic',
        ),
        migrations.RemoveField(
            model_name='category',
            name='classifcation',
        ),
        migrations.DeleteModel(
            name='Classification',
        ),
    ]
