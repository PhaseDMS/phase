from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transmittals', '0047_auto_20160224_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outgoingtransmittal',
            name='latest_revision',
            field=models.ForeignKey(on_delete=models.PROTECT, verbose_name='Latest revision', to='transmittals.OutgoingTransmittalRevision', null=True),
        ),
        migrations.AlterField(
            model_name='transmittal',
            name='latest_revision',
            field=models.ForeignKey(on_delete=models.PROTECT, verbose_name='Latest revision', to='transmittals.TransmittalRevision', null=True),
        ),
    ]
