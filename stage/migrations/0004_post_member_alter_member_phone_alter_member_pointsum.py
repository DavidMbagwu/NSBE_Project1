# Generated by Django 5.0.6 on 2024-07-03 19:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0003_member_pointsum'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='member',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='points', to='stage.member'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='pointsum',
            field=models.IntegerField(blank=True),
        ),
    ]
