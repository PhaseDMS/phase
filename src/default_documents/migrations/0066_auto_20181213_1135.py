# Generated by Django 1.11.16 on 2018-12-13 10:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('default_documents', '0065_auto_20181213_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contractordeliverablerevision',
            name='transmittal',
        ),
        migrations.RemoveField(
            model_name='gtgmetadatarevision',
            name='transmittal',
        ),
    ]
