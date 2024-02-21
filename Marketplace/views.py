from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='Marketplace/index.html')


class Contact(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='Marketplace/contact.html')
