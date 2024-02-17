from datetime import datetime

from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils.translation import gettext_lazy as _

current_year = datetime.now().year
Year_Choices = tuple(zip(range(current_year - 100, current_year + 1), range(current_year - 100, current_year + 1)))[
               ::-1]

Month_CHOICES = (
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December"),
)


class Experience(models.Model):
    title = models.CharField(_('Title'), max_length=50, blank=False)
    company_name = models.CharField(_('Company Name'), max_length=50, blank=True, null=True)
    city = models.CharField(_('City'), max_length=10, blank=True, null=True)
    country = models.CharField(_('Province or country'), max_length=10, blank=True, null=True)
    start_year = models.IntegerField(_('Start Year'), choices=Year_Choices, blank=True, null=True)
    start_month = models.CharField(_('Start Month'), choices=Month_CHOICES, blank=True, null=True, max_length=10)
    end_year = models.IntegerField(_('End Year'), choices=Year_Choices, blank=True, null=True)
    end_month = models.CharField(_('End Month'), choices=Month_CHOICES, blank=True, null=True, max_length=10)
    is_present = models.BooleanField(_('I am currently working in this role'), default=False)
    industry = models.CharField(_('Industry'), max_length=50, blank=True, null=True)
    description = models.TextField(_('Description'), blank=True, null=True)

    # relation
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Education(models.Model):
    school = models.CharField(_('School'), max_length=50, blank=False)
    degree = models.CharField(_('Degree'), max_length=50, blank=True, null=True)
    field_of_study = models.CharField(_('Field of Study'), max_length=200, blank=True, null=True)
    city = models.CharField(_('City'), max_length=10, blank=True, null=True)
    country = models.CharField(_('Province or country'), max_length=10, blank=True, null=True)
    start_year = models.IntegerField(_('Start Year'), choices=Year_Choices, blank=True, null=True)
    start_month = models.CharField(_('Start Month'), choices=Month_CHOICES, blank=True, null=True, max_length=10)
    end_year = models.IntegerField(_('End Year'), choices=Year_Choices, blank=True, null=True)
    end_month = models.CharField(_('End Month'), choices=Month_CHOICES, blank=True, null=True, max_length=10)
    grade = models.FloatField(_('Grade'))
    description = models.TextField(_('Description'), blank=True, null=True)
    # relation
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)

    def __str__(self):
        return self.school


class Certificate(models.Model):
    name = models.CharField(_('Name'), max_length=50, blank=False)
    issuing_organization = models.CharField(_('Issuing Organization'), max_length=20, blank=False)
    issue_year = models.IntegerField(_('Issue Year'), choices=Year_Choices, blank=True, null=True)
    issue_month = models.CharField(_('Issue Month'), choices=Month_CHOICES, blank=True, null=True, max_length=10)
    expiration_year = models.IntegerField(_('Expiration Year'), choices=Year_Choices, blank=True, null=True)
    expiration_month = models.CharField(_('Expiration Month'), choices=Month_CHOICES, blank=True, null=True,
                                        max_length=10)
    Credential_id = models.CharField(_('Credential Id'), max_length=20, blank=True, null=True)
    credential_url = models.URLField(_('Credential URL'))
    # relation
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Skill(models.Model):
    title = models.CharField(_('Title'), max_length=50, blank=False)
    # relation
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Language(models.Model):
    language = models.CharField(_('Language'), max_length=20, blank=False)
    Proficiency_Choice = (
        ('elementary', 'Elementary proficiency'),
        ('limited', 'Limited working proficiency'),
        ('professional', 'Professional working proficiency'),
        ('full', 'Full professional proficiency'),
        ('native', 'Native or bilingual proficiency'),
    )
    proficiency = models.CharField(_('Proficiency'), max_length=20, blank=False, choices=Proficiency_Choice)
    # relation
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)

    def __str__(self):
        return self.language


class Portfolio(models.Model):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    birth_date = models.DateField(_('Birth date'), blank=True, null=True)
    phone_number = models.CharField(_('Phone number'), max_length=20, blank=True, null=True)
    country = models.CharField(_('Province or country'), max_length=10, blank=True, null=True)
    city = models.CharField(_('City'), max_length=10, blank=True, null=True)
    postal_code = models.CharField(_('Postal code'), max_length=10, blank=True, null=True)
    street_address = models.CharField(_('Street address'), blank=True, null=True, max_length=50)
    professional_summary = models.TextField(_('Professional Summary'), blank=True, null=True)
    linkedin = models.URLField(_('LinkedIn'), blank=True, null=True)
    github = models.URLField(_('GitHub'), blank=True, null=True)
    twitter = models.URLField(_('Twitter'), blank=True, null=True)
    facebook = models.URLField(_('Facebook'), blank=True, null=True)
    interests = models.TextField(_('Interests'), blank=True, null=True)
    # Relations
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_birth_date(self):
        if self.birth_date is not None:
            month = "{}".format(self.birth_date.month).zfill(2)
            day = "{}".format(self.birth_date.day).zfill(2)
            year = "{}".format(self.birth_date.year)
        else:
            month = '01'
            day = '01'
            year = '0001'

        return '{}-{}-{}'.format(year, month, day)

    def __str__(self):
        return self.user.username
