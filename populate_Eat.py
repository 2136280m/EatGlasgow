import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'EatGlasgow.settings')

import django

django.setup()
import random
from EatGlasgowApp.models import *
from django.contrib.auth.models import User


def populate():
    users = [
        {"username": "nickyvo", "pass": "12345abc", "avatar": "defUser.jpeg", "status": 2},
        {"username": "alex", "pass": "12345abc", "avatar": "defUser.jpeg", "status": 1},
        {"username": "tom", "pass": "12345abc", "avatar": "defUser.jpeg", "status": 2},
        {"username": "caroline", "pass": "12345abc", "avatar": "defUser.jpeg", "status": 1},
        {"username": "guest", "pass": "12345abc", "avatar": "defUser.jpeg", "status": 1},
        {"username": "guest1", "pass": "12345abc", "avatar": "defUser.jpeg", "status": 1}
    ]

    restaurants = [
        {"name": "Weather Spoon", "owner": "tom", "photo": "defRes.jpeg",
         "cuisine": "WE", "address": "123 Byres Road Glasgow",
         "price": 2, "status": 1,"description":"Our destination Grill offers a fresh and sophisticated seasonal menu with brasserie-style service. The Bar upstairs features an exclusive Champagne Room and Cigar Terrace, offering an extensive drinks list of classic cocktails and wine from around the world. For up-to-date menus and drinks lists, please visit our website."},
        {"name": "Cook Indi", "owner": "tom", "photo": "defRes.jpeg",
         "cuisine": "AS", "address": "123 Great Western Road Glasgow",
         "price": 2, "status": 1,"description":"Our destination Grill offers a fresh and sophisticated seasonal menu with brasserie-style service. The Bar upstairs features an exclusive Champagne Room and Cigar Terrace, offering an extensive drinks list of classic cocktails and wine from around the world. For up-to-date menus and drinks lists, please visit our website."},
        {"name": "Dumpling Monkey", "owner": "tom", "photo": "defRes.jpeg",
         "cuisine": "AS", "address": "123 Dumbarton Road Glasgow",
         "price": 1, "status": 1,"description":"Our destination Grill offers a fresh and sophisticated seasonal menu with brasserie-style service. The Bar upstairs features an exclusive Champagne Room and Cigar Terrace, offering an extensive drinks list of classic cocktails and wine from around the world. For up-to-date menus and drinks lists, please visit our website."},
        {"name": "Neighbourhood", "owner": "tom", "photo": "defRes.jpeg",
         "cuisine": "AS", "address": "123 Argyle Street Glasgow",
         "price": 2, "status": 1,"description":"Our destination Grill offers a fresh and sophisticated seasonal menu with brasserie-style service. The Bar upstairs features an exclusive Champagne Room and Cigar Terrace, offering an extensive drinks list of classic cocktails and wine from around the world. For up-to-date menus and drinks lists, please visit our website."},
        {"name": "Pickled Ginger", "owner": "nickyvo", "photo": "defRes.jpeg",
         "cuisine": "AS", "address": "123 St.Vincent Street Glasgow",
         "price": 3, "status": 1,"description":"Our destination Grill offers a fresh and sophisticated seasonal menu with brasserie-style service. The Bar upstairs features an exclusive Champagne Room and Cigar Terrace, offering an extensive drinks list of classic cocktails and wine from around the world. For up-to-date menus and drinks lists, please visit our website."},
    ]
    promotions = [{"ResID": 1, "des": "50% off"},
                  {"ResID": 1, "des": "25% off first bill"},
                  {"ResID": 2, "des": "50% off"},
                  {"ResID": 3, "des": "50% off"},
                  ]

    reviews = [
        {"user": "guest", "resID": 1, "content": "Nice one", "photo": "defRev.jpeg",
         "rating": 2},
        {"user": "guest", "resID": 2, "content": "Great one", "photo": "defRev.jpeg",
         "rating": 3},
        {"user": "guest", "resID": 1, "content": "Okay", "photo": "defRev.jpeg",
         "rating": 2}
    ]

    replies = [
        {"revID": 1, "owner": "nickyvo", "content": "Thanks"},
        {"revID": 2, "owner": "tom", "content": "Thank you"},
    ]

    for user in users:
        add_user_and_profile(user["username"], user["pass"], user["avatar"], user["status"])

    for res in restaurants:
        add_res(res["owner"], res["name"], res["photo"], res["cuisine"], res["address"], res["price"], res["description"])

    for pro in promotions:
        add_pro(pro["ResID"], pro["des"])

    for rev in reviews:
        add_review(rev["user"], rev["resID"], rev["content"], rev["photo"], rev["rating"])

    for rep in replies:
        add_reply(rep["revID"], rep["owner"], rep["content"])


def add_user_and_profile(username, password, avatar, statusstatus):
    u = User.objects.create_user(username, email=None, password=None)
    u.set_password(password)
    u.save()
    up = UserProfile.objects.create()
    up.user_id = u.id
    up.avatar = "profile_images\\"+avatar
    up.status = statusstatus
    up.save()


def add_res(owner, name, photo, cuisine, add, price, d):
    u = User.objects.get(username=owner)
    r = Restaurant.objects.create(owner_id=u.id)
    r.name = name
    r.photo = "restaurant_images\\"+photo
    r.cuisine = cuisine
    r.streetAddress = add
    r.priceRange = price
    r.description = d
    r.save()


def add_pro(res, content):
    r = Restaurant.objects.get(resID=res)
    p = Promotion.objects.create(resID_id=r.resID)
    p.content = content
    p.save()


def add_review(user, res, content, photo, rating):
    u = User.objects.get(username=user)
    res = Restaurant.objects.get(resID=res)
    rev = Review.objects.create(userID_id=u.id, resID_id=res.resID)
    rev.content = content
    rev.photo = "review_images\\defRev.jpeg"
    rev.rating = rating
    rev.save()


def add_reply(rev, owner, content):
    rev = Review.objects.get(revID=rev)
    u = User.objects.get(username=owner)
    rep = Reply.objects.create(revID_id=rev.revID, ownerID_id=u.id)
    rep.content = content
    rep.save()

    # Start execution here!


if __name__ == '__main__':
    print("Starting EatGlasgow population script...")
    populate()
    print("Done")