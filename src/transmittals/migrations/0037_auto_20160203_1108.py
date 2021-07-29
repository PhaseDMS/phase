from django.db import migrations, models
import metadata.fields


class Migration(migrations.Migration):

    dependencies = [
        ('transmittals', '0036_auto_20160203_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trsrevision',
            name='contract_number_old',
            field=metadata.fields.ConfigurableChoiceField(max_length=8, null=True, verbose_name='Contract Number', list_index='CONTRACT_NBS', blank=True),
        ),
    ]
