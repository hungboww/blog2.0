# Generated by Django 3.2.10 on 2022-07-14 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_forummodel_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forummodel',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
