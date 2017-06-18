# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20161121173054 on 2017-06-18 18:18
from __future__ import unicode_literals

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('scanapp', '0004_delete_emegencycontact'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='driver_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bus',
            name='teacher_incharge_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
