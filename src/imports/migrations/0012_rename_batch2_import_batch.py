# Generated by Django 3.2.7 on 2021-09-16 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0011_remove_import_batch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='import',
            old_name='batch2',
            new_name='batch',
        ),
    ]
