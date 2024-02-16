from datetime import datetime

from django.contrib.auth.models import AbstractUser
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
    company_name = models.CharField(_('Company Name'), max_length=50, blank=True)
    city = models.CharField(_('City'), max_length=10, null=True, blank=True)
    country = models.CharField(_('Province or country'), max_length=10, null=True, blank=True)
    start_year = models.IntegerField(_('Start Year'), choices=Year_Choices, null=True, blank=True)
    start_month = models.CharField(_('Start Month'), choices=Month_CHOICES, null=True, blank=True, max_length=10)
    end_year = models.IntegerField(_('End Year'), choices=Year_Choices, null=True, blank=True)
    end_month = models.CharField(_('End Month'), choices=Month_CHOICES, null=True, blank=True, max_length=10)
    is_present = models.BooleanField(_('I am currently working in this role'), default=False)
    industry = models.CharField(_('Industry'), max_length=50, null=True, blank=False)
    description = models.TextField(_('Description'), null=True, blank=True)

    # relation
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Education(models.Model):
    school = models.CharField(_('School'), max_length=50, blank=False)
    degree = models.CharField(_('Degree'), max_length=50, blank=True)
    field_of_study = models.CharField(_('Field of Study'), max_length=200, blank=True)
    city = models.CharField(_('City'), max_length=10, null=True, blank=True)
    country = models.CharField(_('Province or country'), max_length=10, null=True, blank=True)
    start_year = models.IntegerField(_('Start Year'), choices=Year_Choices, null=True, blank=True)
    start_month = models.CharField(_('Start Month'), choices=Month_CHOICES, null=True, blank=True, max_length=10)
    end_year = models.IntegerField(_('End Year'), choices=Year_Choices, null=True, blank=True)
    end_month = models.CharField(_('End Month'), choices=Month_CHOICES, null=True, blank=True, max_length=10)
    grade = models.FloatField(_('Grade'))
    description = models.TextField(_('Description'), null=True, blank=True)
    # relation
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.school


class Certificate(models.Model):
    name = models.CharField(_('Name'), max_length=50, blank=False)
    issuing_organization = models.CharField(_('Issuing Organization'), max_length=20, blank=False)
    issue_year = models.IntegerField(_('Issue Year'), choices=Year_Choices, null=True, blank=True)
    issue_month = models.CharField(_('Issue Month'), choices=Month_CHOICES, null=True, blank=True, max_length=10)
    expiration_year = models.IntegerField(_('Expiration Year'), choices=Year_Choices, null=True, blank=True)
    expiration_month = models.CharField(_('Expiration Month'), choices=Month_CHOICES, null=True, blank=True,
                                        max_length=10)
    Credential_id = models.CharField(_('Credential Id'), max_length=20, blank=True)
    credential_url = models.URLField(_('Credential URL'))
    # relation
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Skill(models.Model):
    title = models.CharField(_('Title'), max_length=50, blank=False)
    # relation
    user = models.ForeignKey('User', on_delete=models.CASCADE)

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
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.language


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    background_image = models.ImageField(upload_to='background/', blank=True)
    birth_date = models.DateField(_('Birth date'), null=True, blank=True)
    phone_number = models.CharField(_('Phone number'), max_length=20, null=True, blank=True)
    country = models.CharField(_('Province or country'), max_length=10, null=True, blank=True)
    city = models.CharField(_('City'), max_length=10, null=True, blank=True)
    postal_code = models.CharField(_('Postal code'), max_length=10, null=True, blank=True)
    street_address = models.CharField(_('Street address'), null=True, blank=True, max_length=50)
    professional_summary = models.TextField(_('Professional Summary'), null=True, blank=True)
    linkedin = models.URLField(_('LinkedIn'), null=True)
    github = models.URLField(_('GitHub'), null=True)
    twitter = models.URLField(_('Twitter'), null=True)
    facebook = models.URLField(_('Facebook'), null=True)
    interests = models.TextField(_('Interests'), null=True, blank=True)

    def get_birth_date(self):
        month = "{}".format(self.birth_date.month).zfill(2)
        day = "{}".format(self.birth_date.day).zfill(2)
        return '{}-{}-{}'.format(self.birth_date.year, month, day)

    def __str__(self):
        return self.username
