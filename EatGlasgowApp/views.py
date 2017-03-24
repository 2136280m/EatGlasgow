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
    ##make random order restaurand
    context_dict = {'RestaurantList': RestaurantList}
    ##make it to dict
    return render(request, 'index.html', context_dict)

def about(request):
    return render(request, 'about.html')

def restaurant(request, RestaurantID):
    ##check if it is post
    if request.method == 'POST':
        ##only user allow the post any thing
        if request.user.is_authenticated():
            ##new Restaurant
            workingR=Restaurant.objects.get(resID=RestaurantID)
            ##the Restaurant that current work with
            if request.user==workingR.owner:
                ##only that restaurant owner allow to make reply of reviews
                form = ReviewUploadForm(request.POST, request.FILES)
                ##get the form to reply
                rev=Review.objects.get(revID=request.POST.get('ReviewID'))
                ##make reply
                NewReply=Reply.objects.create(revID = rev, ownerID=workingR.owner)
                NewReply.content=request.POST.get('review_text')
                NewReply.save()
            else:
                ##create new Review
                NewReview=Review.objects.create(userID = request.user, resID=workingR)
                NewReview.content = request.POST.get('review_text')
                NewReview.rating = request.POST.get('rating')
                try:##check if there is photo uploaded
                    NewReview.photo=request.FILES['photo']
                except Reply.DoesNotExist:
                    pass
                NewReview.save()
    RestaurantList = Restaurant.objects.get(resID=RestaurantID)  ##RestaurantList by RestaurantID
    ReviewList = Review.objects.filter(resID=RestaurantID).order_by('-reviewDate')  ##ReviewList by RestaurantID
    replyList = []##return review
    replyid=[]##use for check is there is reply in review
    for x in ReviewList:
        try:
            replyList.append(Reply.objects.get(revID=x.revID))
            replyid.append(Reply.objects.get(revID=x.revID).revID.revID)
        except Reply.DoesNotExist:
            pass
    
    context_dict = {'RestaurantList': RestaurantList, 'ReviewList': ReviewList, 'replyList': replyList, 'replyid':replyid}

    return render(request, 'restaurant.html', context_dict)

def restaurantEditor(request, RestaurantID):
    try:
        ##get Restaurant to edit
        Editor = Restaurant.objects.get(resID=RestaurantID)
    except :
        return render(request, 'Restaurant_Editor.html')
    ##check if it is a post
    if request.method == 'POST':
        ##check the post is make by owner
        if request.user==Editor.owner:
            Editor.name=request.POST.get('name')
            Editor.cuisine=request.POST.get('cuisine')
            Editor.streetAddress=request.POST.get('address')
            Editor.priceRange=request.POST.get('Price')
            Editor.openingHour=request.POST.get('OH')
            Editor.status=request.POST.get('status')
            try:##check if there is photo uploaded
                Editor.photo=request.FILES['photo']
            except :
                pass
            Editor.save()
    return render(request, 'Restaurant_Editor.html', {'RestaurantList':Editor})


def user_login(request):
    if request.method == 'POST':##check if it is post
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:##user is active?
                login(request, user)## login
                return HttpResponseRedirect(reverse('index'))##back to index
            else:
                return HttpResponse("Your account is disabled")
        else:
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'login.html')


def registration(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():##check if it can regisate
            user = user_form.save()###create user
            user.set_password(user.password)
            user.save()
            NewUserProfile=UserProfile.objects.create()##create profile
            NewUserProfile.user_id=user.id
            NewUserProfile.status=request.POST.get('isOwner')
            NewUserProfile.save()
            registered = True
    else:
        user_form = UserForm()
    return render(request, 'registration.html', {'registered': registered, 'user_form': user_form})


def random_restaurant():
    restaurant_list = list(Restaurant.objects.filter(status=1))##all restaurant that opening
    if len(restaurant_list) > 0:##check there is Restaurant
        restaurant_list = []
        maxID = Restaurant.objects.last().resID##get the max id
        if maxID != None and maxID > 4:
            randomint = set()  ##generat random int without repeating
        while len(randomint) < 5:
            randomint.add(randint(1, maxID))##gererate 5 random number
        for RN in randomint:
            restaurant_list.append(Restaurant.objects.get(resID=RN))##make list to send to website
    
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
        ##check the post is make by owner
        if request.user.userprofile.status == 2 :
            G=Restaurant.objects.create(owner=request.user)
            G.name=request.POST.get('name')
            G.cuisine=request.POST.get('cuisine')
            G.streetAddress=request.POST.get('address')
            G.priceRange=request.POST.get('Price')
            G.openingHour=request.POST.get('OH')
            G.status=request.POST.get('status')
            try:##check if there is photo uploaded
                G.photo=request.FILES['photo']
            except :
                pass
            G.save()
    return render(request, 'addRestaurant.html')

def search_results(request):
    context = {}
    # this is what search bar is called
    search = request.GET.get('search')
    context['results'] = Restaurant.objects.filter(name__icontains=search)
    return render(request, 'results.html', context=context)

@login_required
def your_restaurant(request):
    if request.method == 'POST':##check if it is post
        rest=Restaurant.objects.get(resID=request.POST.get('Rid'))##get all the restaurant of the owner
        if (rest.status==1):##if it open, mark it close
            rest.status=-1
            rest.save()
        elif (rest.status==-1):##if it close, mark it open
            rest.status=1
            rest.save()
    return render(request, 'your_restaurant.html', {'RestaurantList':Restaurant.objects.filter(owner=request.user, status=1)|Restaurant.objects.filter(owner=request.user, status=-1)})
    ##select * from Restaurant where owner=request.use and (status=1or status=-1)





def test(request):
    return render(request, 'test.html')
    
def searchtest(request, keyword):
    RestaurantList = {'RestaurantList': Restaurant.objects.filter(name__icontains=keyword)}
    print(RestaurantList)
    return render(request, 'searchresult.html', RestaurantList)

