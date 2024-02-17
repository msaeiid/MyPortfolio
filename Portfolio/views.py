from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from Portfolio.forms import AboutForm, ProfileForm
from Portfolio.models import Portfolio


class PortfolioView(TemplateView):
    model = Portfolio
    template_name = 'Portfolio/index.html'

    def get(self, request, *args, **kwargs):
        portfolio = get_object_or_404(Portfolio, user__username=kwargs.get('pk', 'admin'))

        context = {'portfolio': portfolio}
        return self.render_to_response(context)


class AboutView(LoginRequiredMixin, TemplateView):
    model = Portfolio
    template_name = 'Portfolio/index.html'

    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(Portfolio, user=request.user)
        form = AboutForm(request.POST or None, instance=instance, files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect(reverse_lazy('home'))

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return super(AboutView, self).dispatch(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'Portfolio/index.html'

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect(reverse_lazy('home'))

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return super(ProfileView, self).dispatch(request, *args, **kwargs)
