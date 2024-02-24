from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from Portfolio.models import Portfolio, Certificate, Experience, Education, Skill


class AboutForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = [
            'avatar',
            'resume',
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
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'resume': forms.FileInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'phone_number': forms.DateInput(attrs={'class': 'form-control'}),
            'country': forms.DateInput(attrs={'class': 'form-control'}),
            'city': forms.DateInput(attrs={'class': 'form-control'}),
            'hide_sensitive': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'postal_code': forms.DateInput(attrs={'class': 'form-control'}),
            'street_address': forms.DateInput(attrs={'class': 'form-control'}),
            'professional_summary': forms.Textarea(attrs={'class': 'form-control'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
            'github': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter': forms.URLInput(attrs={'class': 'form-control'}),
            'facebook': forms.URLInput(attrs={'class': 'form-control'}),
        }


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'})
        }


class InterestForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['interests', ]
        widgets = {
            'interests': forms.Textarea(attrs={'class': 'form-control'})
        }


class CertificateForm(ModelForm):
    class Meta:
        model = Certificate
        fields = ['name', 'issuing_organization', 'issue_year', 'issue_month', 'expiration_year', 'expiration_month',
                  'Credential_id', 'credential_url']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'issuing_organization': forms.TextInput(attrs={'class': 'form-control'}),
            'issue_year': forms.Select(attrs={'class': 'form-control'}),
            'issue_month': forms.Select(attrs={'class': 'form-control'}),
            'expiration_year': forms.Select(attrs={'class': 'form-control'}),
            'expiration_month': forms.Select(attrs={'class': 'form-control'}),
            'Credential_id': forms.TextInput(attrs={'class': 'form-control'}),
            'credential_url': forms.URLInput(attrs={'class': 'form-control'})
        }


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'company_name', 'city', 'country', 'start_year', 'start_month',
                  'end_year', 'end_month', 'is_present', 'industry', 'description']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'start_year': forms.Select(attrs={'class': 'form-control'}),
            'start_month': forms.Select(attrs={'class': 'form-control'}),
            'end_year': forms.Select(attrs={'class': 'form-control'}),
            'end_month': forms.Select(attrs={'class': 'form-control'}),
            'is_present': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'industry': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ['school', 'degree', 'field_of_study', 'city', 'country', 'start_year', 'start_month',
                  'end_year', 'end_month', 'grade', 'description']

        widgets = {
            'school': forms.TextInput(attrs={'class': 'form-control'}),
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'start_year': forms.Select(attrs={'class': 'form-control'}),
            'start_month': forms.Select(attrs={'class': 'form-control'}),
            'end_year': forms.Select(attrs={'class': 'form-control'}),
            'end_month': forms.Select(attrs={'class': 'form-control'}),
            'grade': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['title', ]
        widgets = {
            'title': forms.Select(attrs={'class': 'form-control'})
        }
