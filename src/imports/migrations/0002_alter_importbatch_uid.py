# Generated by Django 3.2.4 on 2021-06-30 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importbatch',
            name='uid',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
