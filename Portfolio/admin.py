from django.contrib import admin

from Portfolio.models import Portfolio, Experience, Education, Certificate, Skill, Language


# Register your models here.
@admin.register(Portfolio)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'title', 'company_name')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'school', 'degree')


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'name', 'issuing_organization')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('portfolio',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'language', 'proficiency')
