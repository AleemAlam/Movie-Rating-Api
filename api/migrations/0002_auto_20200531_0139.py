# Generated by Django 3.0.6 on 2020-05-30 20:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('user', 'movie')},
        ),
        migrations.AlterIndexTogether(
            name='rating',
            index_together={('user', 'movie')},
        ),
    ]
