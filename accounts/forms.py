from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from accounts.models import UserProfile


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class EditProfileForm(ModelForm):
    class Meta:

        model = User
        fields = (
            'email',
            'first_name',
            'last_name'
        )

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile

        fields = ('bio', 'gender', 'image', 'background_Image')

