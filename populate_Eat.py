import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'EatGlasgow.settings')

import django
django.setup()
import random
from EatGlasgowApp.models import UserProfile,Owner,Restaurant,Promotion,Review,Reply
from django.contrib.auth.models import User
def populate():

   users = [
       {"username": "nickyvo", "pass": "12345abc", "avatar": "defUser.jpeg", "status": 1},
       {"username": "alex", "pass": "12345abc", "avatar": "defUser.jpeg", "status": 1},
       {"username": "tom", "pass": "12345abc", "avatar": "defUser.jpeg", "status": 1},
       {"username": "caroline", "pass": "12345abc", "avatar": "defUser.jpeg", "status": 1},
       {"username": "guest", "pass": "12345abc", "avatar": "defUser.jpeg", "status": 1},
       {"username": "guest1", "pass": "12345abc", "avatar": "defUser.jpeg", "status": 1}
   ]

   owners = [{"username": "nickyvo"}, {"username": "alex"},
             {"username": "tom"}, {"username": "caroline"}]
   restaurants = [
       {"name": "Weather Spoon", "owner": "nickyvo", "photo": "defRes.jpeg",
                "cuisine": "WE", "address": "123 Byres Road Glasgow",
                "price": 2, "status": 1},
       {"name": "Cook Indi", "owner": "tom", "photo": "defRes.jpeg",
        "cuisine": "AS", "address": "123 Great Western Road Glasgow",
        "price": 2, "status": 1},
       {"name": "Dumpling Monkey", "owner": "caroline", "photo": "defRes.jpeg",
        "cuisine": "AS", "address": "123 Dumbarton Road Glasgow",
        "price": 1, "status": 1},
       {"name": "Neighbourhood", "owner": "alex", "photo": "defRes.jpeg",
        "cuisine": "AS", "address": "123 Argyle Street Glasgow",
        "price": 2, "status": 1},
       {"name": "Pickled Ginger", "owner": "nickyvo", "photo": "defRes.jpeg",
        "cuisine": "AS", "address": "123 St.Vincent Street Glasgow",
        "price": 3, "status": 1},
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
       {"revID": 1, "owner": "nicky", "content": "Thanks"},
       {"revID": 2, "owner": "tom", "content": "Thank you"},
   ]

   # Print out
   for c in User.objects.all():
       print("- {0} - {1}".format(str(c), str(c)))

   for user in users:
        add_user_and_profile(user["username"], user["pass"], user["avatar"])

        # Print out
   for c in User.objects.all():
       print("- {0} - {1}".format(str(c), str(c)))

   for owner in owners:
       add_owner(owner["username"])
   # Print out
   for c in Owner.objects.all():
       print("- {0} - {1}".format(str(c), str(c.isOwner)))

   for res in restaurants:
       add_res(res["owner"],res["name"],res["photo"],res["cuisine"],res["address"], res["price"])

   for c in Restaurant.objects.all():
       print("- {0} - {1}".format(str(c), str(c.status)))
   for pro in promotions:
       add_pro(pro["ResID"],pro["des"])
   for c in Promotion.objects.all():
       print("- {0} - {1}".format(str(c), str(c.status)))
   for rev in reviews:
       add_review(rev["user"],rev["resID"],rev["content"],rev["photo"],rev["rating"])
   for c in Review.objects.all():
       print("- {0} - {1}".format(str(c), str(c.status)))

   for rep in replies:
       add_reply(rep["revID"],rep["owner"],rep["content"])

   for c in Reply.objects.all():
       print("- {0} - ".format(str(c)))

def add_user_and_profile(username,password,avatar):
    u = User.objects.create_user(username, email=None, password=None)
    u.set_password(password)
    u.save()
    up = UserProfile.objects.create()
    up.user_id = u.id
    up.avatar = avatar
    up.save()


def add_owner(username):
    u = User.objects.get(username=username)
    o = Owner.objects.create()
    o.user_id = u.id
    o.save()

def add_res(owner,name,photo,cuisine,add,price):
    u = User.objects.get(username=owner)
    r = Restaurant.objects.create()
    r.owner_id = u.id
    r.name = name
    r.photo = photo
    r.cuisine = cuisine
    r.streetAddress = add
    r.priceRange = price
    r.save()

def add_pro(res,content):
    p = Promotion.objects.create()
    r = Restaurant.objects.get(res)
    p.resID_id = r.id
    p.content = content
    p.save()

def add_review(user,res,content,photo,rating):
    rev = Review.objects.create()
    u = User.objects.get(username=user)
    res = Restaurant.objects.get(res)
    rev.userID_id = u.id
    rev.resID_id = res.id
    rev.content = content
    rev.rating =rating
    rev.save()

def add_reply(rev,owner,content):
    rev = Review.objects.get(rev)
    u = User.objects.get(username=owner)
    rep = Reply.objects.create()
    rep.revID_id = rev.id
    rep.ownerID_id = u.id
    rep.content = content
    rep.save()
 
 # Start execution here!
if __name__ == '__main__':
    print("Starting EatGlasgow population script...")
    populate()
    print("Done")