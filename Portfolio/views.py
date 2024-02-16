from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from Portfolio.forms import AboutForm
from Portfolio.models import User


class PortfolioView(TemplateView):
    model = User
    template_name = 'Portfolio/index.html'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=kwargs.get('pk', 'admin'))
        context = {'user': user}
        return self.render_to_response(context)


class AboutView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'Portfolio/index.html'

    @login_required
    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(User, username='admin')
        form = AboutForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
        return redirect(reverse_lazy('home'))

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return super(AboutView, self).dispatch(request, *args, **kwargs)
