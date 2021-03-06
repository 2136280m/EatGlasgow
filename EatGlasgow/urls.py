"""EatGlasgow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from EatGlasgowApp import views

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^$', views.index, name='index'),
                  url(r'^about/', views.about, name='about'),
                  url(r'^restaurant-(?P<RestaurantID>[\w\-]+)$', views.restaurant, name='restaurant'),
                  url(r'^restaurant-(?P<RestaurantID>[\w\-]+)/edit-restaurant$', views.restaurantEditor, name='restaurantEditor'),

                  url(r'^login$', views.user_login, name='login'),
                  url(r'^logout/$', views.user_logout, name='logout'),
                  url(r'^registration$', views.registration, name='registration'),
                  url(r'^addRestaurant$', views.add_restaurant, name='addRestaurant'),
                  url(r'^results/$', views.search_results, name='results'),
                  url(r'^your-restaurant', views.your_restaurant, name='your_restaurant'),
                  
                  url(r'^search/(?P<keyword>[\w\-]+)$', views.searchtest, name='ST'),
                  
                  
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
