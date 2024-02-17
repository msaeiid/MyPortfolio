from django.contrib.auth.models import User
from django.forms import ModelForm
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


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]
