# Generated by Django 3.2.4 on 2021-06-16 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_channel_external_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='sponsored_images'),
        ),
    ]
