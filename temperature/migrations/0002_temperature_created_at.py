# Generated by Django 3.2.13 on 2022-05-08 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temperature', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperature',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
