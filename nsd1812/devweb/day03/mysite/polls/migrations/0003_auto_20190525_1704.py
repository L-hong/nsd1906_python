# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-25 17:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='q',
            new_name='question',
        ),
    ]
