from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile




class UserLoginForm(forms.Form):
    """Form to login the user"""
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class UserRegistrationForm(UserCreationForm):
    """ Form used to sign up and register a new user"""
    username = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=200)
    password1 = forms.CharField(label="Password",  widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
   
    
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
        
        

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
       
class ProfileRegistrationForm(forms.ModelForm):
    
    address_one = forms.CharField(max_length=100, label="Address")
    address_two = forms.CharField(max_length=100, label="Address")
    city = forms.CharField(max_length=50)
    postcode = forms.CharField(max_length=20)
    country = forms.CharField(max_length=100)
    experience = forms.CharField(max_length=300)
    style = forms.CharField(max_length=200)
    wood_source = forms.BooleanField()
    
    
    class Meta:
        model = Profile
        fields = ['address_one', 'address_two', 'city', 'country', 'experience', 'style', 'wood_source', 'postcode']
