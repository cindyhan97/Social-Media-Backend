# Generated by Django 4.0.2 on 2022-03-04 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endterm', '0009_rename_user_id_publicchat_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicchat',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publicChat_user', to='endterm.appuser'),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poster', to='endterm.appuser'),
        ),
    ]
