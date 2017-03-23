from django import forms
from django.contrib.auth.models import User
from EatGlasgowApp.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    isOwner = forms.BooleanField()

	# meta class describes additional properties about a particular class
	# to which it belongs
    class Meta:
        model = User
        fields = ('username', 'email', 'password','isOwner')