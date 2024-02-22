from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView
from Marketplace.forms import SignUpForm, AddItemForm
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


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'Marketplace/signup.html'
    success_url = 'market/login'


class AddItemView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = 'Marketplace/add_item.html'
    form_class = AddItemForm

    def get_context_data(self, **kwargs):
        context = super(AddItemView, self).get_context_data()
        context['page_title'] = 'New Item'

        return context

    def get_success_url(self):
        return reverse_lazy('Marketplace:item_detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(AddItemView, self).form_valid(form)


class DashboardView(TemplateView):
    model = Item
    template_name = 'Marketplace/dashboard/index.html'

    def get(self, request, *args, **kwargs):
        items = Item.objects.filter(created_by=request.user)

        return render(request, self.template_name, {'items': items})
