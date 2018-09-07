from django import forms
from django.contrib.auth.models import User
from chemex.models import Customer
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class CustomerUserCreationForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('street', 'phone', 'city', 'state', 'zipcode')
