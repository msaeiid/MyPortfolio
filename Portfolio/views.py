from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from Portfolio.forms import AboutForm
from Portfolio.models import User


class PortfolioView(TemplateView):
    model = User
    template_name = 'Portfolio/index.html'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=kwargs.get('pk', 'admin'))
        context = {'user': user}
        return self.render_to_response(context)


class AboutView(UpdateView):
    model = User
    template_name = 'Portfolio/index.html'
    form_class = AboutForm

    def get_success_url(self):
        pk = get_object_or_404(User, pk=self.kwargs['pk'])
        return reverse_lazy('home', kwargs={'pk': pk})



