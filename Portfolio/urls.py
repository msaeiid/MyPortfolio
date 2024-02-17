from django.contrib.auth.views import LogoutView
from django.urls import path

from MyPortfolio import settings
from Portfolio.views import PortfolioView, AboutView, ProfileView

urlpatterns = [
    path('', PortfolioView.as_view(), name='home'),
    path('about_edit/', AboutView.as_view(), name='about_edit'),
    path('profile_edit/', ProfileView.as_view(), name='profile_edit'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
]
