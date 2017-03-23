from django.contrib import admin
from EatGlasgowApp.models import UserProfile
from EatGlasgowApp.models import *
# Register your models here


admin.site.register(UserProfile)
admin.site.register(Restaurant)
admin.site.register(Promotion)
admin.site.register(Review)
admin.site.register(Reply)
