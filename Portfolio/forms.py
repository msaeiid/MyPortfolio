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
