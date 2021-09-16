# Generated by Django 3.2.7 on 2021-09-16 09:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0004_importbatch_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importbatch',
            name='uid',
            field=models.CharField(default=uuid.uuid4, max_length=200, primary_key=True, serialize=False),
        ),
    ]
