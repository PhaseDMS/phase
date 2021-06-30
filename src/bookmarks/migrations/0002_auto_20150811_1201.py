from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='category',
            field=models.ForeignKey(on_delete=models.PROTECT, to='categories.Category'),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(on_delete=models.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
