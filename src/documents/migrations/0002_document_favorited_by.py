from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favorites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='favorited_by',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='favorites.Favorite', blank=True),
        ),
    ]
