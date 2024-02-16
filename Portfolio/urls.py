from django.urls import path

from Portfolio.views import PortfolioView, AboutView

urlpatterns = [
    path('<slug:pk>/', PortfolioView.as_view(), name='home'),
    path('<slug:pk>/about_edit', AboutView.as_view(), name='about_edit')
]
