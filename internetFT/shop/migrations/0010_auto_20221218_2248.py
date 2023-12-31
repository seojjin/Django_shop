# Generated by Django 3.2 on 2022-12-18 22:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0009_delete_recomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='item',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
