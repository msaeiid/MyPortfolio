from django.urls import path

from Marketplace.views import Index, Contact, ItemDetail

app_name = 'Marketplace'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('contact/', Contact.as_view(), name='contact'),
    path('items/<int:pk>', ItemDetail.as_view(), name='item_detail')

]
