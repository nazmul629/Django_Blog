from django import forms
from .models import articale,author,comment
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm

class createForm(forms.ModelForm):
    class Meta:
        model= articale
        fields= "__all__"
        exclude = ['articale_author']

class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields=[
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        ]

class creatrAuthor(forms.ModelForm):
    class Meta:
        model = author
        fields = '__all__'
        exclude = ['name']
    

class commentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = '__all__'
        exclude = ['post']
    
       