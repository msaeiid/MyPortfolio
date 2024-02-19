from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib import messages

from Portfolio.forms import AboutForm, ProfileForm, InterestForm, CertificateForm, EducationForm, ExperienceForm
from Portfolio.models import Portfolio, Experience, Certificate, Skill, Language, Education


class PortfolioView(TemplateView):
    model = Portfolio
    template_name = 'Portfolio/index.html'

    def get(self, request, *args, **kwargs):
        portfolio = get_object_or_404(Portfolio, user__username=kwargs.get('pk', 'admin'))

        context = {'portfolio': portfolio,
                   'about_form': AboutForm(instance=request.user.portfolio),
                   'profile_form': ProfileForm(instance=request.user),
                   'interest_form': InterestForm(instance=request.user.portfolio),
                   }
        return self.render_to_response(context)


class AboutView(LoginRequiredMixin, TemplateView):
    model = Portfolio
    template_name = 'Portfolio/index.html'

    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(Portfolio, user=request.user)
        form = AboutForm(request.POST or None, instance=instance, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'profile has been updated')
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
            messages.success(request, 'about section has been updated')
        return redirect(reverse_lazy('home'))

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return super(ProfileView, self).dispatch(request, *args, **kwargs)


class InterestsView(LoginRequiredMixin, TemplateView):
    model = Portfolio
    template_name = 'Portfolio/index.html'

    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(Portfolio, user=request.user)
        form = InterestForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'interest section has been updated')
        return redirect(reverse_lazy('home'))

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return super(InterestsView, self).dispatch(request, *args, **kwargs)


class UpdateView(LoginRequiredMixin, TemplateView):
    template_name = 'Portfolio/update.html'

    def get(self, request, *args, **kwargs):
        class_name = str.capitalize(request.path.replace('/', ''))
        model = eval(class_name)
        objects = get_list_or_404(model, portfolio=request.user.portfolio)
        form = eval(f'{class_name}Form')
        update_forms = {obj.id: form(instance=obj) for obj in objects}
        context = {'portfolio': request.user.portfolio,
                   'form': form,
                   'update_forms': update_forms,
                   'template': request.path.replace('/', ''),
                   'url': request.path,
                   'is_update_page': True}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        extracted_data = str.capitalize(request.path.replace('/', ' ')).strip().split(' ')
        class_name = str.capitalize(extracted_data[0])
        operation = extracted_data[1]
        model = eval(str.capitalize(class_name))
        form = eval(f'{str.capitalize(class_name)}Form')
        if operation == 'add':
            form = form(request.POST or None)
            if form.is_valid():
                form.cleaned_data['portfolio_id'] = request.user.portfolio.id
                obj = model.objects.create(**form.cleaned_data)
                messages.success(request, f'{obj} has been updated to {extracted_data[0]}')
        elif operation == 'update':
            pk = extracted_data[2]
            instance = model.objects.get(pk=pk)
            form = form(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
        return redirect(reverse_lazy(f'{extracted_data[0]}'))

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return super(UpdateView, self).dispatch(request, *args, **kwargs)
