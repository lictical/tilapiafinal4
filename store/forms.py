from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateNewList(forms.Form):#allow us to generate automatically new forms
    name = forms.CharField(label="Name", max_length=200)#creates an imput of a name
    check = forms.BooleanField(required=False)#creates check button

class CreateKassen(forms.Form):#allow us to generate automatically new forms
    name = forms.CharField(label="Name", max_length=200)  # creates an imput of a name
    check = forms.BooleanField(required=False)  # creates check button

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =  ['username', 'email', 'password1', 'password2']


