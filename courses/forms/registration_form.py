from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
    username   = forms.CharField(max_length=50, required=True)
    email      = forms.EmailField(max_length=150, required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def clean_email(self):
        email = self.cleaned_data['email']
        user = None
        try:
            user  = User.objects.get(email=email)
        except:
            return email
        
        if user is not None:
            raise ValidationError("User Already Exists")