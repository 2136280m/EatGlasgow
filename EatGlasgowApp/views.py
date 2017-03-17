from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    
    restaurantExample = {"RestaurantID":1, "Name":"Myrestaurant", "Cuisine":"Chinese",
        "StressAdress":"Chinese", "PriceRange":"Expensive", "OpeningHours":"7am-8am",
        "Status":1,"logo":"logo.jpg"}
        
        
    
    response = render(request, 'index.html', restaurantExample)
    # Render the response and send it back!
    return response
    #return HttpResponse("Rango says hey there partner!")
    
def index1(request, IndexPage):
    context_dict = {'Index': IndexPage}
    # Render the response and send it back!
    return render(request, 'index.html', context_dict)
    #return HttpResponse("Rango says hey there partner!")
    
def NormalPageStyle(request):
	return render(request, 'NormalPageStyle.css')
		