# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20161121173054 on 2017-06-10 06:51
from __future__ import unicode_literals

from django.db import migrations
import scanapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('scanapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='latitude',
            field=scanapp.models.CommaSeparatedFloatField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='bus',
            name='longitude',
            field=scanapp.models.CommaSeparatedFloatField(max_length=500, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together=set([('student_biometric_id', 'bus')]),
        ),
    ]
