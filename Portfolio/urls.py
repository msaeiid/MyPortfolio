from django.urls import path

from Portfolio.views import PortfolioView, AboutView

urlpatterns = [
    path('', PortfolioView.as_view(), name='home'),
    path('about_edit/', AboutView.as_view(), name='about_edit')
]
