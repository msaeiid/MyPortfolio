from django.urls import path

from Portfolio.views import home_view

urlpatterns = [
    path('', home_view, name='home')
]
