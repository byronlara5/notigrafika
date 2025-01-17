# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-17 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_ads_spot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='ads/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='spot',
            field=models.CharField(choices=[('center', 'Centro'), ('index', 'Inicio'), ('detail', 'Articulos'), ('section', 'Secciones'), ('hidden', 'Oculta')], default='hidden', max_length=100),
        ),
    ]
