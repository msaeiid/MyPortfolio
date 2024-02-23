from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

from Marketplace.models import Item


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Username', 'class': 'w-full py-4 px-6 rounded-xl'}))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your email address', 'class': 'w-full py-4 px-6 rounded-xl'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Your password', 'class': 'w-full py-4 px-6 rounded-xl'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Repeat password', 'class': 'w-full py-4 px-6 rounded-xl'}))


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Username', 'class': 'w-full py-4 px-6 rounded-xl'}))

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Your password', 'class': 'w-full py-4 px-6 rounded-xl'}))


INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class AddItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'name', 'description', 'price', 'image']
        widgets = {
            'category': forms.Select(attrs={'class': INPUT_CLASSES}),
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES}),
            'price': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASSES}),
        }


class UpdateItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'image', 'is_sold']
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES}),
            'price': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASSES}),
        }
