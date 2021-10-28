# Generated by Django 3.2.8 on 2021-10-28 02:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_rename_liked_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='user_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.CharField(default='like', max_length=6),
        ),
    ]