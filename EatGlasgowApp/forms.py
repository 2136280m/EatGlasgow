from django import forms
from django.contrib.auth.models import User
from EatGlasgowApp.models import UserProfile, Restaurant, Review


class UserForm(forms.ModelForm):
    CHOICES = ((2, 'I am a Owner',), (1, 'I am a normal User'))
    password = forms.CharField(widget=forms.PasswordInput())
    isOwner =  forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

	# meta class describes additional properties about a particular class
	# to which it belongs
    class Meta:
        model = User
        fields = ('username', 'email', 'password','isOwner')

class RestaurantForm(forms.ModelForm):
	CUISINE_CHOICE = (('WE', 'Western'), ('AS', 'Asian'), ('ME', 'Middle Eastern'),)
	RANGE_CHOICE = ((0, 'Not Rated'), (1, 'Low Price'), (2, 'Affordable'), (3, 'Fancy'),)
	RESTAURANT_STATUS_CHOICE = ((1, 'Open'), (0, 'Close down'), (-1, 'Close'))

	#name, streedAdress, opening hourt(input)
	name = forms.CharField(max_length=128, help_text="Please enter the name of restaurant")
	cuisine = forms.ChoiceField(widget=forms.RadioSelect, choices=CUISINE_CHOICE)
	streetAdress = forms.CharField(max_length=128, help_text="Please enter the adress of restaurant")
	priceRange = forms.ChoiceField(widget=forms.RadioSelect, choices=RANGE_CHOICE)
	openingHours = forms.CharField(max_length=128, help_text="Please enter the opening hours of restaurant")
	status = forms.ChoiceField(widget=forms.RadioSelect, choices=RESTAURANT_STATUS_CHOICE)

	class Meta():
		model = Restaurant
		fields = ('name', 'cuisine', 'priceRange', 'status', 'streetAdress', 'openingHours' )