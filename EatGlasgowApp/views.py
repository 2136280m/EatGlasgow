from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.models import User
from EatGlasgowApp.models import *
from EatGlasgowApp.forms import *
from django import template
from django.core.urlresolvers import reverse

from random import randint

def index(request):
    RestaurantList = random_restaurant()
    context_dict = {'RestaurantList': RestaurantList}
    return render(request, 'index.html', context_dict)


def about(request):
    return render(request, 'about.html')


def restaurant(request, RestaurantID):
    if request.method == 'POST':
        if request.user.is_authenticated():
            workingR=Restaurant.objects.get(resID=RestaurantID)
            if request.user==workingR.owner:
                form = ReviewUploadForm(request.POST, request.FILES)
                rev=Review.objects.get(revID=request.POST.get('ReviewID'))
                NewReply=Reply.objects.create(revID = rev, ownerID=workingR.owner)
                NewReply.content=request.POST.get('review_text')
                NewReply.save()
            else:
                NewReview=Review.objects.create(userID = request.user, resID=workingR)
                NewReview.content = request.POST.get('review_text')
                NewReview.rating = request.POST.get('rating')
                NewReview.photo=request.FILES['photo']
                NewReview.save()
    RestaurantList = Restaurant.objects.get(resID=RestaurantID)  ##RestaurantList by RestaurantID
    ReviewList = Review.objects.filter(resID=RestaurantID).order_by('-reviewDate')  ##ReviewList by RestaurantID
    replyList = []
    replyid=[]
    for x in ReviewList:
        try:
            replyList.append(Reply.objects.get(revID=x.revID))
            replyid.append(Reply.objects.get(revID=x.revID).revID.revID)
        except Reply.DoesNotExist:
            pass
    
    context_dict = {'RestaurantList': RestaurantList, 'ReviewList': ReviewList, 'replyList': replyList, 'replyid':replyid}

    return render(request, 'restaurant.html', context_dict)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is disabled")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'login.html', {})


def registration(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            NewUserProfile=UserProfile.objects.create()
            NewUserProfile.user_id=user.id
            NewUserProfile.status=request.POST.get('isOwner')
            NewUserProfile.save()
            registered = True
    else:
        user_form = UserForm()
    return render(request, 'registration.html', {'registered': registered, 'user_form': user_form})


def random_restaurant():
    restaurant_list = list(Restaurant.objects.filter(status=1))
    if restaurant_list.count(Restaurant) > 0:
        restaurant_list = []
        maxID = Restaurant.objects.last().resID
        if maxID != None and maxID > 5:
            randomint = set()  ##generat random int without repeating
        while len(randomint) < 5:
            randomint.add(randint(1, maxID))
        for RN in randomint:
            restaurant_list.append(Restaurant.objects.get(resID=RN))
    return restaurant_list


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('index'))

@login_required
def add_restaurant(request):
    if request.method == 'POST':
        addRestaurant_form = RestaurantForm(data=request.POST)
        if addRestaurant_form.is_valid():
            restaurant = addRestaurant_form.save()
            NewRestaurant = Restaurant.objects.create()
            NewRestaurant.cuisine = request.POST.get('cuisine')
            NewRestaurant.priceRange = request.POST.get('priceRange')
            NewRestaurant.status = request.POST.get('status')

            NewRestaurant.save()

    else:
        addRestaurant_form = RestaurantForm()
    return render(request, 'addRestaurant.html', {'addRestaurant_form': addRestaurant_form})

def search_results(request):
    context = {}
    # this is what search bar is called
    search = request.GET.get('search')
    context['results'] = Restaurant.objects.filter(name__icontains=search)
    return render(request, 'results.html', context=context)

@login_required
def your_restaurant(request):
    if request.method == 'POST':
        rest=Restaurant.objects.get(resID=request.POST.get('Rid'))
        if (rest.status==1):
            print(rest)
            rest.status=-1
            rest.save()
        elif (rest.status==-1):
            print(rest)
            rest.status=1
            rest.save()
    return render(request, 'your_restaurant.html', {'RestaurantList':Restaurant.objects.filter(owner=request.user, status=1)|Restaurant.objects.filter(owner=request.user, status=-1)})

