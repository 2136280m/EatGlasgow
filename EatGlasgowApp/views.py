from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.models import User
from EatGlasgowApp.models import *
from EatGlasgowApp.forms import *
from django.core.urlresolvers import reverse

from random import randint


def index(request):
    RestaurantList = random_restaurant()
    context_dict = {'RestaurantList': RestaurantList}
    return render(request, 'index.html', context_dict)


def about(request):
    return render(request, 'about.html')


def restaurant(request, RestaurantID):
    RestaurantList = Restaurant.objects.get(resID=RestaurantID)  ##RestaurantList by RestaurantID
    ReviewList = Review.objects.filter(resID=RestaurantID).order_by('-reviewDate')  ##ReviewList by RestaurantID
    replyList = []
    for x in ReviewList:
        try:
            replyList.append(Reply.objects.get(revID=x.revID))
        except Reply.DoesNotExist:
            replyList.append(None)
    print(replyList)
    context_dict = {'RestaurantList': RestaurantList, 'ReviewList': ReviewList, 'replyList': replyList}

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
    restaurant_List = list(Restaurant.objects.all())
    if restaurant_List.count(Restaurant) > 0:
        restaurant_List = []
        maxID = Restaurant.objects.last().resID
        if maxID != None and maxID > 5:
            randomint = set()  ##generat random int without repeating
        while len(randomint) < 5:
            randomint.add(randint(1, maxID))
        for RN in randomint:
            restaurant_List.append(Restaurant.objects.get(resID=RN))
    return restaurant_List


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('index'))


def add_restaurant(request):
    return render(request, 'addRestaurant.html')


def search_results(reuqest):


    context = {}
    # this is what search bar is called
    search = request.GET.get('search')
    context['results'] = Book.objects.filer(name__icontains=search)
    return render(request, 'Results.html', context=context)
