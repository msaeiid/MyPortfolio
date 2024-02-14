from django.shortcuts import get_object_or_404, render

from Portfolio.models import User, Language, Experience, Education, Certificate, Skill


def home_view(request):
    user = get_object_or_404(User, username='admin')
    languages = Language.objects.filter(user=user)
    experiences = Experience.objects.filter(user=user)
    certificates = Certificate.objects.filter(user=user)
    skills = Skill.objects.filter(user=user)
    educations = Education.objects.filter(user=user)
    context = {
        'user': user,
        'languages': languages,
        'experiences': experiences,
        'certificates': certificates,
        'skills': skills,
        'educations': educations,
    }

    return render(request=request, template_name='Portfolio/index.html', context=context)

# Create your views here.
