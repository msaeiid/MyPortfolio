from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView, UpdateView
from Marketplace.forms import SignUpForm, AddItemForm, UpdateItemForm, MessageForm
from Marketplace.models import Item, Category, Conversation


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
        return render(request, template_name='Marketplace/conversation/contact.html')


class ItemDetail(DetailView):
    model = Item
    template_name = 'Marketplace/item/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ItemDetail, self).get_context_data(**kwargs)
        context['related_items'] = Item.objects.filter(category=context['item'].category, is_sold=False).exclude(
            pk=context['item'].pk)[0:3]
        return context


class AddItemView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = 'Marketplace/item/add.html'
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
    template_name = 'Marketplace/item/confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        item = get_object_or_404(Item, pk=self.kwargs.get('pk', None), created_by=self.request.user)
        item.delete()
        return reverse_lazy(self.success_url)


class UpdateItemView(LoginRequiredMixin, UpdateView):
    model = Item
    template_name = 'Marketplace/item/add.html'
    form_class = UpdateItemForm

    def get_context_data(self, **kwargs):
        context = super(UpdateItemView, self).get_context_data()
        context['page_title'] = 'Update'
        return context

    def get_object(self):
        return get_object_or_404(Item, pk=self.kwargs.get('pk'), created_by=self.request.user)


class ListItemView(TemplateView):
    model = Item
    template_name = 'Marketplace/item/list.html'

    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', '')
        items = Item.objects.filter(is_sold=False)
        categories = Category.objects.all()
        category_id = int(request.GET.get('category', 0))
        if query:
            items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
        if category_id:
            items = items.filter(category_id=category_id)
        context = {'items': items, 'categories': categories, 'category_id': category_id, 'query': query}
        return render(request, self.template_name, context)


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'Marketplace/account/signup.html'
    success_url = 'market/login'


class DashboardView(LoginRequiredMixin, TemplateView):
    model = Item
    template_name = 'Marketplace/dashboard/index.html'

    def get(self, request, *args, **kwargs):
        items = Item.objects.filter(created_by=request.user)

        return render(request, self.template_name, {'items': items})


class AddConversation(LoginRequiredMixin, TemplateView):
    template_name = 'Marketplace/conversation/new.html'

    def post(self, request, *args, **kwargs):
        item = get_object_or_404(Item, pk=kwargs.get('item_pk'))
        form = MessageForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            message = form.save(commit=False)
            message.conversation = conversation
            message.created_by = request.user
            message.save()

            return redirect('Marketplace:item_detail', pk=item.pk)

    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, pk=kwargs.get('item_pk'))
        if item.created_by == request.user:
            return redirect('market:dashboard')

        conversations = item.conversations.filter(members__in=[request.user.id])
        if conversations:
            return redirect('Marketplace:conversation_detail', pk=conversations.first().id)
        form = MessageForm()
        return render(request, self.template_name, {'form': form})


class InboxView(LoginRequiredMixin, TemplateView):
    template_name = 'Marketplace/conversation/inbox.html'
    model = Conversation

    def get(self, request, *args, **kwargs):
        conversations = request.user.conversations.all()

        context = {'conversations': conversations}
        return render(request, self.template_name, context)


class ConversationDetail(LoginRequiredMixin, TemplateView):
    model = Conversation
    template_name = 'Marketplace/conversation/detail.html'

    def get(self, request, *args, **kwargs):
        conversation = Conversation.objects.get(pk=kwargs.get('pk'))
        form = MessageForm()

        context = {'conversation': conversation, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.conversation = Conversation.objects.get(pk=kwargs.get('pk'))
            message.created_by = request.user
            message.save()
        return redirect('Marketplace:conversation_detail', pk=kwargs.get('pk'))
