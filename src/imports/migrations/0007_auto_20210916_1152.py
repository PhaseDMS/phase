# Generated by Django 3.2.7 on 2021-09-16 09:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0006_copy_uuid_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importbatch',
            name='uid',
        ),
        migrations.AlterField(
            model_name='importbatch',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
