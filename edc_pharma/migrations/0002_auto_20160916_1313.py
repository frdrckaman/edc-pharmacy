# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-16 11:13
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edc_pharma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispense',
            name='prepared_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 16, 13, 13, 36, 646546)),
        ),
        migrations.AlterField(
            model_name='historicalpatient',
            name='consent_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 16, 13, 13, 36, 641198)),
        ),
        migrations.AlterField(
            model_name='historicalpatient',
            name='initials',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('[A-Z]{2,3}')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='consent_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 16, 13, 13, 36, 641198)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='initials',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('[A-Z]{2,3}')]),
        ),
    ]
