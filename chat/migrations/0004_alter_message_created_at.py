# Generated by Django 4.2.7 on 2024-01-19 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_message_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]