# Generated by Django 3.2.4 on 2021-07-02 11:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0002_alter_importbatch_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importbatch',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
