from django.urls import path

from Portfolio.views import home_view, about_view

urlpatterns = [
    path('', home_view, name='home'),
    path('aboutme/', about_view, name='about_me')
]
