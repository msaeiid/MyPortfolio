from django.contrib.auth.views import LogoutView
from django.urls import path

from MyPortfolio import settings
from Portfolio.views import PortfolioView, AboutView, ProfileView, InterestsView, UpdateView

app_name = 'Portfolio'
urlpatterns = [
    path('', PortfolioView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('interest/', InterestsView.as_view(), name='interest'),

    path('experience/', UpdateView.as_view(), name='experience'),
    path('experience/add', UpdateView.as_view(), name='experience_add'),
    path('experience/update/<int:pk>', UpdateView.as_view(), name='experience_update'),
    path('experience/delete/<int:pk>', UpdateView.as_view(), name='experience_delete'),

    path('certificate/', UpdateView.as_view(), name='certificate'),
    path('certificate/add', UpdateView.as_view(), name='certificate_add'),
    path('certificate/update/<int:pk>', UpdateView.as_view(), name='certificate_update'),
    path('certificate/delete/<int:pk>', UpdateView.as_view(), name='certificate_delete'),

    path('education/', UpdateView.as_view(), name='education'),
    path('education/add', UpdateView.as_view(), name='education_add'),
    path('education/update/<int:pk>', UpdateView.as_view(), name='education_update'),
    path('education/delete/<int:pk>', UpdateView.as_view(), name='education_delete'),

    path('skill/', UpdateView.as_view(), name='skill'),
    path('skill/add', UpdateView.as_view(), name='skill_add'),
    path('skill/update/<int:pk>', UpdateView.as_view(), name='skill_update'),
    path('skill/delete/<int:pk>', UpdateView.as_view(), name='skill_delete'),

    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
]
