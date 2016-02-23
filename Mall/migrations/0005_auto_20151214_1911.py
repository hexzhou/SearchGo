# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import Mall.models


class Migration(migrations.Migration):

    dependencies = [
        ('Mall', '0004_auto_20151213_1244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '目录分类', 'verbose_name': '目录分类'},
        ),
        migrations.AlterModelOptions(
            name='commodity',
            options={'verbose_name_plural': '图片商品', 'verbose_name': '图片商品'},
        ),
        migrations.AddField(
            model_name='commodity',
            name='color_features',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='commodity',
            name='shape_features',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='commodity',
            name='img',
            field=models.ImageField(upload_to=Mall.models.uploade_path_handler, blank=True, verbose_name='pic_path'),
        ),
    ]
