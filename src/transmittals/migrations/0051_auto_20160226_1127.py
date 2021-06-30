from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transmittals', '0050_make_entities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trsrevision',
            name='originator_new',
            field=models.ForeignKey(on_delete=models.PROTECT, verbose_name='Originator', to='accounts.Entity'),
        ),
    ]
