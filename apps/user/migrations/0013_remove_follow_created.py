# Generated by Django 3.2.10 on 2022-07-14 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20220714_0754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='created',
        ),
    ]
