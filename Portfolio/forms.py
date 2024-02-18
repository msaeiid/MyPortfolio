from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, SelectDateWidget, NumberInput
from Portfolio.models import Portfolio


class AboutForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = [
            'avatar',
            'birth_date',
            'phone_number',
            'country',
            'city',
            'postal_code',
            'street_address',
            'professional_summary',
            'linkedin',
            'github',
            'twitter',
            'facebook',
            'interests', ]

    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super(AboutForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]
