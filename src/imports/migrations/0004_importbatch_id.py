# Generated by Django 3.2.7 on 2021-09-16 09:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0003_alter_importbatch_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='importbatch',
            name='id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]