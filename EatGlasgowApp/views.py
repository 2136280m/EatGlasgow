from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.models import User
from EatGlasgowApp.models import UserProfile
from EatGlasgowApp.forms import UserForm

def index(request):
    RestaurantList={}
    restaurantExample = {"RestaurantID":1, "Name":"Apple", "Cuisine":"Chinese",
        "StressAdress":"Glasogw", "PriceRange":"Expensive", "OpeningHours":"7am-8am",
        "Status":1,"logo":"logo.jpg"}
    # Render the response and send it back!
    return render(request, 'index.html', restaurantExample)

def about(request):
	return render(request, 'about.html')
	
def restaurant(request, RestaurantID):
	
	restaurantExample = {"RestaurantID":1, "Name":"Apple", "Cuisine":"Chinese",
    "StressAdress":"Chinese", "PriceRange":"Expensive", "OpeningHours":"7am-8am",
    "Status":1,"logo":"logo.jpg"}
	try:
		if(int(RestaurantID)==restaurantExample["RestaurantID"]):
			return render(request,'restaurant.html', restaurantExample)
		else:
			return HttpResponse("There is not such restaurant")
	except ValueError:
		return HttpResponse("There is not such restaurant")


def login(request):
    return render(request, 'login.html')
    """#f the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:   
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object..."""
		
def registration(request):
	registered = False
	
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
	
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
	else:
		user_form = UserForm()
			
	return render(request, 'registration.html',
			{'registered': registered,'user_form': user_form})

	
	
	
	
	
	
	
	
	
	
