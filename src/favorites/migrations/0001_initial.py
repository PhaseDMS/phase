from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_view_date', models.DateTimeField(auto_now_add=True)),
                ('document', models.ForeignKey(on_delete=models.PROTECT, to='documents.Document')),
                ('user', models.ForeignKey(on_delete=models.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
