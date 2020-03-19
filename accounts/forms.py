from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from accounts.models import Profile


class UserLoginForm(forms.Form):
    """Form to login the user"""
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class UserRegistrationForm(forms.ModelForm):
    """ Form used to sign up and register a new user"""
 
    first_name = forms.CharField(max_length=12)
    last_name = forms.CharField(max_length=12)
    email = forms.EmailField(max_length=200)
    username = forms.CharField( max_length=150,)
    address1 = forms.CharField(max_length=100, label="Address Line 1")
    address2 = forms.CharField(max_length=100, label="Address Line 2")
    city = forms.CharField(max_length=50)
    country = forms.CharField(max_length=100)
    password1 = forms.CharField(label="Password",  widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
    experience = forms.CharField(max_length=300)
    style = forms.CharField(max_length=200)
    source = forms.BooleanField(label="Is your wood legally sourced?")
    
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'address1', 'address2', 'city', 'country', 'experience', 'style', 'source')
        
        
        

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError('This Email is already in our system ')
        return email
        
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise ValidationError('Please confirm your password')
            
        if password1 != password2:
            raise ValidationError('Your password must match')
        
        return password2
       
    
