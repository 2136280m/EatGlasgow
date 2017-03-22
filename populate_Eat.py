import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'EatGlasgow.settings')

import django
django.setup()
import random
from EatGlasgow.models import UserProfile,Owner,Restaurant,Promotion,Review,Reply
from django.contrib.auth.models import User
def populate():
   # First, we will create lists of dictionaries containing the pages
   # we want to add into each category.
   # Then we will create a dictionary of dictionaries for our categories.
   # This might seem a little bit confusing, but it allows us to iterate
   # through each data structure, and add the data to our models.
   
   python_pages = [
       {"title": "Official Python Tutorial",
        "url":"http://docs.python.org/2/tutorial/"},
       {"title":"How to Think like a Computer Scientist",
        "url":"http://www.greenteapress.com/thinkpython/"},
       {"title":"Learn Python in 10 Minutes",
        "url":"http://www.korokithakis.net/tutorials/python/"} ]
   
   django_pages = [
       {"title":"Official Django Tutorial",
        "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
       {"title":"Django Rocks",
        "url":"http://www.djangorocks.com/"},
       {"title":"How to Tango with Django",
        "url":"http://www.tangowithdjango.com/"} ]
   
   other_pages = [
       {"title":"Bottle",
        "url":"http://bottlepy.org/docs/dev/"},
       {"title":"Flask",
        "url":"http://flask.pocoo.org"} ]
   
   cats = {"Python": {"pages": python_pages},
           "Django": {"pages": django_pages},
           "Other Frameworks": {"pages": other_pages} }

   users = [
       {"username":"nicky", "pass": "12345abc", "avatar": "defUser.jpeg", "status": 1},
       {"username": "alex", "pass": "12345abc", "avatar": "defUser.jpeg", "status": 1},
       {"username": "tom", "pass": "12345abc", "avatar": "defUser.jpeg", "status": 1},
       {"username": "caroline", "pass": "12345abc", "avatar": "defUser.jpeg", "status": 1},
       {"username": "guest", "pass": "12345abc", "avatar": "defUser.jpeg", "status": 1},
       {"username": "guest1", "pass": "12345abc", "avatar": "defUser.jpeg", "status": 1}
            ]

   owners = [{"username": "nicky"}, {"username": "alex"},
             {"username": "tom"}, {"username": "caroline"}]
   restaurants = [
       {"name": "Weather Spoon", "owner": "nicky", "photo": "defRes.jpeg",
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
       {"name": "Pickled Ginger", "owner": "nicky", "photo": "defRes.jpeg",
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

   # If you want to add more catergories or pages,
   # add them to the dictionaries above.
   
   # The code below goes through the cats dictionary, then adds each category,
   # and then adds all the associated pages for that category.
   # if you are using Python 2.x then use cats.iteritems() see
   # http://docs.quantifiedcode.com/python-anti-patterns/readability/
   # for more information about how to iterate over a dictionary properly.
   
   for user in users.items():


       for cat, cat_data in cats.items():
           if (cat == "Python"):
               c = add_cat(cat, 128, 64)
           elif (cat == "Django"):
               c = add_cat(cat, 64, 32)
           else:
               c = add_cat(cat, 32, 16)
           for p in cat_data["pages"]:
               add_page(c, p["title"], p["url"])
   
   # Print out the categories we have added.
   for c in Category.objects.all():
       for p in Page.objects.filter(category=c):
           print("- {0} - {1}".format(str(c), str(p)))

def add_user(username,password,avatar):
    u=User.objects.get_or_create()

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views= random.randrange(5, 20)
    p.save()
    return p
 
def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_cat(name,views,likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c
 
 # Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
