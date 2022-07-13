# Generated by Django 3.2.10 on 2022-07-13 10:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_alter_forummodel_stt'),
    ]

    operations = [
        migrations.AddField(
            model_name='forummodel',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='forummodel',
            name='time_post',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]