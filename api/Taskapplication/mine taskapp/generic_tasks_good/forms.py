from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField( required=True)
    class Meta:
        model = User
        fields = ["username", "password1","password2","email"]
        widgets = {
                    'username': forms.TextInput(attrs={
                        'class': 'form-control', 
                        'placeholder': 'Enter your username', 
                        'aria-label': 'Username', 
                        'title': 'Your unique username for logging in',
                        'data-bs-toggle': 'tooltip',
                        'data-bs-placement': 'top',
                        'data-bs-title': 'Username should be unique',
                    }),
                    'password1': forms.PasswordInput(attrs={
                        'class': 'form-control', 
                        'placeholder': 'Enter your password', 
                        'aria-label': 'Password', 
                        'title': 'Password should be strong',
                        'data-bs-toggle': 'tooltip',
                        'data-bs-placement': 'top',
                        'data-bs-title': 'Use a strong password (at least 8 characters)',
                    }),
                    'password2': forms.PasswordInput(attrs={
                        'class': 'form-control', 
                        'placeholder': 'Confirm your password', 
                        'aria-label': 'Password confirmation', 
                        'title': 'Re-enter your password',
                        'data-bs-toggle': 'tooltip',
                        'data-bs-placement': 'top',
                        'data-bs-title': 'Must match the first password field',
                    }),
                    'email': forms.EmailInput(attrs={
                        'class': 'form-control', 
                        'placeholder': 'Enter your email address', 
                        'aria-label': 'Email', 
                        'title': 'Your email address for account communication',
                        'data-bs-toggle': 'tooltip',
                        'data-bs-placement': 'top',
                        'data-bs-title': 'Ensure it’s a valid email address',
                    }),
                }
        
