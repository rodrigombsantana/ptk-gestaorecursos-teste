# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-21 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0006_auto_20170721_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='horario_fim',
            field=models.TimeField(default='19:44', verbose_name='Horario Fim'),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='horario_inicio',
            field=models.TimeField(default='19:44', verbose_name='Horario Inicio'),
        ),
    ]
