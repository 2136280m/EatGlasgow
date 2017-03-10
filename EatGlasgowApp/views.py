from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    response = render(request, 'index.html')
    # Render the response and send it back!
    return response
    #return HttpResponse("Rango says hey there partner!")
    
def NormalPageStyle(request):
	return render(request, 'NormalPageStyle.css')
		