# Generated by Django 1.11.16 on 2018-12-13 14:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('default_documents', '0066_auto_20181213_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contractordeliverablerevision',
            name='transmittal_sent_date',
        ),
        migrations.RemoveField(
            model_name='contractordeliverablerevision',
            name='trs_return_code',
        ),
        migrations.RemoveField(
            model_name='gtgmetadatarevision',
            name='transmittal_sent_date',
        ),
        migrations.RemoveField(
            model_name='gtgmetadatarevision',
            name='trs_return_code',
        ),
    ]
