# Generated by Django 3.2.7 on 2021-09-16 10:04

from django.db import migrations
from django.db.migrations.operations.special import RunPython


def copy_import_fks(apps, schema_editor):
    Import = apps.get_model('imports', 'Import')
    for imp in Import.objects.all():
        imp.batch2 = imp.batch
        imp.save()


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0009_import_batch2'),
    ]

    operations = [
        migrations.RunPython(copy_import_fks, migrations.RunPython.noop),
    ]