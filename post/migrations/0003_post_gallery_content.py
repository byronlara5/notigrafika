# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-12 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_remove_post_gallery_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='gallery_content',
            field=models.BooleanField(default=False, verbose_name='Galeria'),
        ),
    ]
