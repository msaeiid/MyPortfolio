from django.forms import ModelForm

from Portfolio.models import User


class AboutForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'avatar',
            'background_image',
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
