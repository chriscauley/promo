# Generated by Django 3.2.4 on 2021-06-22 16:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_channel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='videosponsor',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 6, 22, 16, 57, 24, 587743, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
