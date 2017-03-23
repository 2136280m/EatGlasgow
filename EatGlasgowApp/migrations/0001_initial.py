# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 14:28
from __future__ import unicode_literals

import EatGlasgowApp.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('promotionID', models.AutoField(primary_key=True, serialize=False)),
                ('fromDate', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('toDate', models.DateTimeField(default=EatGlasgowApp.models.one_week_hence)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('status', models.IntegerField(choices=[(1, 'Activating'), (0, 'Deleted'), (-1, 'Expired')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('repID', models.AutoField(primary_key=True, serialize=False)),
                ('repDate', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('content', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('resID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='restaurant_images')),
                ('cuisine', models.CharField(choices=[('WE', 'Western'), ('AS', 'Asian'), ('ME', 'Middle Eastern')], max_length=2)),
                ('streetAddress', models.CharField(blank=True, max_length=100)),
                ('priceRange', models.IntegerField(choices=[(0, 'Not Rated'), (1, 'Low Price'), (2, 'Affordable'), (3, 'Fancy')], default=0)),
                ('openingHour', models.CharField(blank=True, max_length=100)),
                ('status', models.IntegerField(choices=[(1, 'Stored'), (0, 'Deleted'), (-1, 'Closed')], default=1)),
                ('description', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('revID', models.AutoField(primary_key=True, serialize=False)),
                ('reviewDate', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('content', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, upload_to='review_images')),
                ('rating', models.IntegerField(choices=[(0, 'Not Rated'), (1, 'Poor'), (2, 'Okay'), (3, 'Excellent')], default=0)),
                ('status', models.IntegerField(choices=[(1, 'Stored'), (0, 'Deleted')], default=1)),
                ('resID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EatGlasgowApp.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('avatar', models.ImageField(blank=True, upload_to='profile_images')),
                ('status', models.IntegerField(choices=[(1, 'Stored'), (0, 'Deleted')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='EatGlasgowApp.UserProfile')),
                ('isOwner', models.IntegerField(choices=[(1, 'isOwner'), (0, 'isLocked')], default=1)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reply',
            name='ownerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reply',
            name='revID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='EatGlasgowApp.Review'),
        ),
        migrations.AddField(
            model_name='promotion',
            name='resID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EatGlasgowApp.Restaurant'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EatGlasgowApp.Owner'),
        ),
    ]
