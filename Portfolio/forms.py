from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from Portfolio.models import Portfolio, Certificate, Experience, Education, Skill


class AboutForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = [
            'avatar',
            'birth_date',
            'phone_number',
            'country',
            'city',
            'hide_sensitive',
            'postal_code',
            'street_address',
            'professional_summary',
            'linkedin',
            'github',
            'twitter',
            'facebook',
        ]

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

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class InterestForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['interests', ]

    def __init__(self, *args, **kwargs):
        super(InterestForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class CertificateForm(ModelForm):
    class Meta:
        model = Certificate
        fields = ['name', 'issuing_organization', 'issue_year', 'issue_month', 'expiration_year', 'expiration_month',
                  'Credential_id', 'credential_url']

    def __init__(self, *args, **kwargs):
        super(CertificateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'company_name', 'city', 'country', 'start_year', 'start_month',
                  'end_year', 'end_month', 'is_present', 'industry', 'description']

    def __init__(self, *args, **kwargs):
        super(ExperienceForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ['school', 'degree', 'field_of_study', 'city', 'country', 'start_year', 'start_month',
                  'end_year', 'end_month', 'grade', 'description']

    def __init__(self, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['title', ]

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
