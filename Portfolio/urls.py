from django.contrib.auth.views import LogoutView
from django.urls import path

from MyPortfolio import settings
from Portfolio.views import PortfolioView, AboutView, ProfileView, InterestsView, UpdateView

urlpatterns = [
    path('', PortfolioView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('interest/', InterestsView.as_view(), name='interest'),
    path('experience/', UpdateView.as_view(), name='experience'),
    path('certificate/', UpdateView.as_view(), name='certificate'),
    path('education/', UpdateView.as_view(), name='education'),

    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
]
