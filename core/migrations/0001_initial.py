# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='ФИО', max_length=255)),
            ],
            options={
                'verbose_name': 'врач',
                'verbose_name_plural': 'Врачи',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='ФИО', max_length=255)),
                ('start_at', models.DateTimeField(verbose_name='Начало приема')),
                ('doctor', models.ForeignKey(to='core.Doctor', verbose_name='Врач', related_name='entries')),
            ],
            options={
                'ordering': ['-start_at'],
                'verbose_name': 'запись',
                'verbose_name_plural': 'Записи',
            },
        ),
    ]
