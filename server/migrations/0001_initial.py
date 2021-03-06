# Generated by Django 3.2.4 on 2021-06-17 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(max_length=64, unique=True)),
                ('external_username', models.CharField(blank=True, max_length=128, null=True)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('image', models.ImageField(blank=True, null=True, upload_to='sponsored_images')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(max_length=64, unique=True)),
                ('title', models.CharField(blank=True, max_length=264, null=True)),
                ('url', models.TextField()),
                ('channel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.channel')),
            ],
        ),
        migrations.CreateModel(
            name='VideoSponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=256)),
                ('paragraph', models.TextField()),
                ('channel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.channel')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.sponsor')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.video')),
            ],
        ),
        migrations.CreateModel(
            name='SponsorDomain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=64)),
                ('no_promo', models.BooleanField(default=False)),
                ('urls', models.JSONField(default=list)),
                ('sponsor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.sponsor')),
            ],
        ),
    ]
