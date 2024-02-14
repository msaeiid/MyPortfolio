from django.contrib import admin

from Portfolio.models import User, Experience, Education, Certificate, Skill, Language


# Register your models here.
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'company_name')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('user', 'school', 'degree')


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'issuing_organization')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('user', 'title')


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('user', 'language', 'proficiency')
