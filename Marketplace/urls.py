from django.contrib.auth.views import LoginView
from django.urls import path

from Marketplace.forms import LoginForm
from Marketplace.views import Index, Contact, ItemDetail, SignUp, AddItemView

app_name = 'Marketplace'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('contact/', Contact.as_view(), name='contact'),
    path('items/<int:pk>', ItemDetail.as_view(), name='item_detail'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', LoginView.as_view(authentication_form=LoginForm, template_name='Marketplace/login.html'),
         name='login'),
    path('add_item/', AddItemView.as_view(), name='add_item'),

]
