from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transmittals', '0045_auto_20160224_1147'),
        ('documents', '0007_set_metadata_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outgoingtransmittalrevision',
            name='metadata',
            field=models.ForeignKey(on_delete=models.PROTECT, to='transmittals.OutgoingTransmittal'),
        ),
        migrations.AlterField(
            model_name='transmittalrevision',
            name='metadata',
            field=models.ForeignKey(on_delete=models.PROTECT, to='transmittals.Transmittal'),
        ),
    ]
