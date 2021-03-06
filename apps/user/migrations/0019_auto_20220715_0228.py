# Generated by Django 3.2.10 on 2022-07-15 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_createusermodel_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='from_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='followings', to='user.createusermodel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='follow',
            name='to_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='user.createusermodel'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('from_user', 'to_user')},
        ),
        migrations.RemoveField(
            model_name='follow',
            name='follow_to',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='follower',
        ),
    ]
