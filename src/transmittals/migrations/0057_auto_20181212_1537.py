# Generated by Django 1.11.16 on 2018-12-12 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transmittals', '0056_auto_20170524_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='outgoingtransmittal',
            name='external_review_due_date',
            field=models.DateField(blank=True, null=True, verbose_name='External due date'),
        ),
        migrations.AddField(
            model_name='outgoingtransmittal',
            name='purpose_of_issue',
            field=models.CharField(blank=True, choices=[('FR', 'For review'), ('FI', 'For information')], default='FR', max_length=2, verbose_name='Purpose of issue'),
        ),
    ]
