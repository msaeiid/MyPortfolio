from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from Marketplace.models import Item, Category


class Index(TemplateView):
    def get(self, request, *args, **kwargs):
        items = Item.objects.filter(is_sold=False)[0:6]
        categories = Category.objects.all()
        context = {
            'items': items,
            'categories': categories,
        }
        return render(request, template_name='Marketplace/index.html', context=context)


class Contact(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='Marketplace/contact.html')


class ItemDetail(DetailView):
    model = Item
    template_name = 'Marketplace/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ItemDetail, self).get_context_data(**kwargs)
        context['related_items'] = Item.objects.filter(category=context['item'].category, is_sold=False).exclude(
            pk=context['item'].pk)[0:3]
        return context
