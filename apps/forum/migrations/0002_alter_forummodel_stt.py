# Generated by Django 3.2.10 on 2022-07-13 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forummodel',
            name='stt',
            field=models.IntegerField(default=1, max_length=22),
        ),
    ]