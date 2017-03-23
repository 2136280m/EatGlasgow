from django import forms
from django.contrib.auth.models import User
from EatGlasgowApp.models import UserProfile


class UserForm(forms.ModelForm):
    CHOICES = ((2, 'I am a Owner',), (1, 'I am a normal User'))
    password = forms.CharField(widget=forms.PasswordInput())
    isOwner =  forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

	# meta class describes additional properties about a particular class
	# to which it belongs
    class Meta:
        model = User
        fields = ('username', 'email', 'password','isOwner')