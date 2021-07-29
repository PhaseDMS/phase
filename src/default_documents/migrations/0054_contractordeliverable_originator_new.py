from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20160225_1510'),
        ('default_documents', '0053_auto_20160224_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractordeliverable',
            name='originator_new',
            field=models.ForeignKey(on_delete=models.PROTECT, verbose_name='Originator', to='accounts.Entity', null=True),
        ),
    ]
