from django.contrib.auth.views import LoginView
from django.urls import path

from Marketplace.forms import LoginForm
from Marketplace.views import Index, Contact, ItemDetail, SignUp, AddItemView, DashboardView, DeleteItemView, \
    UpdateItemView, ListItemView, AddConversation

app_name = 'Marketplace'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('contact/', Contact.as_view(), name='contact'),
    path('items/<int:pk>', ItemDetail.as_view(), name='item_detail'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', LoginView.as_view(authentication_form=LoginForm, template_name='Marketplace/login.html'),
         name='login'),
    path('add_item/', AddItemView.as_view(), name='add_item'),
    path('<int:pk>/delete_item', DeleteItemView.as_view(), name='delete_item'),
    path('<int:pk>/update_item', UpdateItemView.as_view(), name='update_item'),
    path('list_item/', ListItemView.as_view(), name='list_item'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('new/<int:item_pk>', AddConversation.as_view(), name='new_conversation'),
]
