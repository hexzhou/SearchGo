# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mall', '0002_remove_pic_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commodity',
            name='img_hash',
        ),
        migrations.AddField(
            model_name='commodity',
            name='img',
            field=models.ImageField(upload_to='uploadImages', verbose_name='图片', blank=True),
        ),
    ]
