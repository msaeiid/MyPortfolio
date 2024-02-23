from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView, UpdateView
from Marketplace.forms import SignUpForm, AddItemForm, UpdateItemForm
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
    template_name = 'Marketplace/item_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ItemDetail, self).get_context_data(**kwargs)
        context['related_items'] = Item.objects.filter(category=context['item'].category, is_sold=False).exclude(
            pk=context['item'].pk)[0:3]
        return context


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


class DeleteItemView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('Marketplace:dashboard')
    template_name = 'Marketplace/item_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        item = get_object_or_404(Item, pk=self.kwargs.get('pk', None), created_by=self.request.user)
        item.delete()
        return reverse_lazy(self.success_url)


class UpdateItemView(LoginRequiredMixin, UpdateView):
    model = Item
    template_name = 'Marketplace/add_item.html'
    form_class = UpdateItemForm

    def get_context_data(self, **kwargs):
        context = super(UpdateItemView, self).get_context_data()
        context['page_title'] = 'Update'
        return context

    def get_object(self):
        return get_object_or_404(Item, pk=self.kwargs.get('pk'), created_by=self.request.user)


def list_item_views(request, *args, **kwargs):
    items = Item.objects.filter(is_sold=False)
    if request.method == 'GET':
        context = {'items': items}
        return render(request, 'Marketplace/item_list.html', context)
    elif request.method == 'POST':
        pass


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'Marketplace/signup.html'
    success_url = 'market/login'


class DashboardView(TemplateView):
    model = Item
    template_name = 'Marketplace/dashboard/index.html'

    def get(self, request, *args, **kwargs):
        items = Item.objects.filter(created_by=request.user)

        return render(request, self.template_name, {'items': items})
