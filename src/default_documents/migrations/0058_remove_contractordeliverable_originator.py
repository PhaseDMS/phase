from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_documents', '0057_auto_20160225_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contractordeliverable',
            name='originator',
        ),
    ]
