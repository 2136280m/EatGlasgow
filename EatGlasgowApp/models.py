from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


class UserProfile(models.Model):
    STATUS_CHOICES = (
        (1, 'Stored'),
        (0, 'Deleted'),
    )
    # links userprofile to a user model instance.
    user = models.OneToOneField(User, primary_key=True)
    avatar = models.ImageField(upload_to='profile_images', blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    # override the __unicode__() method to return sth meaningful

    def __str__(self):
        return self.user.username


class Owner(models.Model):
    OWNER_CHOICES = (
        (1, 'isOwner'),
        (0, 'isLocked'),
    )
    user = models.OneToOneField(UserProfile, primary_key=True)

    isOwner = models.IntegerField(choices=OWNER_CHOICES, default=1)

    def __str__(self):
        return self.user.user.username


class Restaurant(models.Model):
    CUISINE_CHOICES = (
        ('WE', 'Western'),
        ('AS', 'Asian'),
        ('ME', 'Middle Eastern'),
    )
    RANGE_CHOICES = (
        (0, 'Not Rated'),
        (1, 'Low Price'),
        (2, 'Affordable'),
        (3, 'Fancy'),
    )
    RES_STATUS_CHOICES = (
        (1, 'Stored'),
        (0, 'Deleted'),
        (-1, 'Closed'),
    )

    resID = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Owner)
    name = models.CharField(max_length=100,blank=False)
    photo = models.ImageField(upload_to='restaurant_images', blank=False)
    cuisine = models.CharField(max_length=2, choices=CUISINE_CHOICES,blank=False)
    streetAddress = models.CharField(max_length=100, blank=True)
    priceRange = models.IntegerField(choices=RANGE_CHOICES, default=0)
    openingHour = models.CharField(max_length=100, blank=True)
    status = models.IntegerField(choices=RES_STATUS_CHOICES, default=1)

    def __str__(self):
        return self.resID


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class Promotion(models.Model):
    PROM_STATUS_CHOICES = (
        (1, 'Activating'),
        (0, 'Deleted'),
        (-1, 'Expired'),
    )
    promotionID = models.AutoField(primary_key=True)
    resID = models.ForeignKey(Restaurant)

    fromDate = models.DateTimeField(default=timezone.now, editable=False)
    toDate = models.DateTimeField(default=one_week_hence)
    description = models.CharField(max_length=200, blank=True)
    status = models.IntegerField(choices=PROM_STATUS_CHOICES, default=1)

    def __str__(self):
        return self.promotionID


class Review(models.Model):
    RATING_CHOICES = (
        (0, 'Not Rated'),
        (1, 'Poor'),
        (2, 'Okay'),
        (3, 'Excellent'),
    )
    STATUS_CHOICES = (
        (1, 'Stored'),
        (0, 'Deleted'),
    )
    revID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User)
    resID = models.ForeignKey(Restaurant)
    reviewDate = models.DateTimeField(default=timezone.now, editable=False)
    content = models.CharField(max_length=200, blank=False)
    photo = models.ImageField(upload_to='review_images', blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return self.revID


class Reply(models.Model):
    repID = models.AutoField(primary_key=True)
    revID = models.OneToOneField(Review)
    ownerID = models.ForeignKey(User)
    repDate = models.DateTimeField(default=timezone.now, editable=False)
    content = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.repID


