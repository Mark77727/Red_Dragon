""" Import modules """

from django import forms
from django.contrib.auth.forms import UserCreationForm

from Account.models import UserProfile

""" Import models """


from django.contrib.auth.models import User

""" Register user form """


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


""" View user profile form """


class EditProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'home_address']

