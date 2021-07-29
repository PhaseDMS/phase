from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Import',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('line', models.IntegerField(verbose_name='Line')),
                ('status', models.CharField(default='new', max_length=50, verbose_name='Status', choices=[('new', 'New'), ('success', 'Success'), ('error', 'Error')])),
                ('errors', models.TextField(null=True, verbose_name='Errors', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImportBatch',
            fields=[
                ('uid', models.UUIDField(max_length=36, serialize=False, editable=False, primary_key=True, blank=True)),
                ('file', models.FileField(upload_to='import_%Y%m%d', verbose_name='File')),
                ('status', models.CharField(default='new', max_length=50, verbose_name='Status', choices=[('new', 'New'), ('started', 'Started'), ('success', 'Success'), ('partial_success', 'Partial success'), ('error', 'Error')])),
                ('created_on', models.DateField(default=django.utils.timezone.now, verbose_name='Created on')),
                ('category', models.ForeignKey(on_delete=models.PROTECT, verbose_name='Category', to='categories.Category')),
            ],
            options={
                'ordering': ['-created_on'],
                'verbose_name': 'Import batch',
                'verbose_name_plural': 'Import batches',
            },
        ),
        migrations.AddField(
            model_name='import',
            name='batch',
            field=models.ForeignKey(on_delete=models.PROTECT, verbose_name='Batch', to='imports.ImportBatch'),
        ),
        migrations.AddField(
            model_name='import',
            name='document',
            field=models.ForeignKey(on_delete=models.PROTECT, blank=True, to='documents.Document', null=True),
        ),
    ]
