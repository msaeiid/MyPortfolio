from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib import messages

from Portfolio.forms import AboutForm, ProfileForm, InterestForm, CertificateForm, EducationForm, ExperienceForm, \
    SkillForm
from Portfolio.models import Portfolio, Experience, Certificate, Skill, Education


class PortfolioView(TemplateView):
    model = Portfolio
    template_name = 'Portfolio/index.html'

    def get(self, request, *args, **kwargs):
        portfolio = get_object_or_404(Portfolio, user__username=kwargs.get('pk', 'admin'))

        context = {'portfolio': portfolio,
                   'about_form': AboutForm(instance=portfolio),
                   'profile_form': ProfileForm(instance=portfolio.user),
                   'interest_form': InterestForm(instance=portfolio),
                   }
        return self.render_to_response(context)


class AboutView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    model = Portfolio
    template_name = 'Portfolio/index.html'
    permission_required = 'Portfolio.change_portfolio'
    permission_denied_message = 'You do not have permission to change portfolio.'

    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(Portfolio, user=request.user)
        form = AboutForm(request.POST or None, instance=instance, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'profile has been updated')
        return redirect(reverse_lazy('Portfolio:home'))


class ProfileView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'Portfolio/index.html'
    permission_required = 'User.change_user'
    permission_denied_message = 'You do not have permission to change user.'

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'about section has been updated')
        return redirect(reverse_lazy('Portfolio:home'))


class InterestsView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    model = Portfolio
    template_name = 'Portfolio/index.html'
    permission_required = 'Portfolio.change_portfolio'
    permission_denied_message = 'You do not have permission to change interest.'

    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(Portfolio, user=request.user)
        form = InterestForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'interest section has been updated')
        return redirect(reverse_lazy('Portfolio:home'))


class UpdateView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'Portfolio/update.html'
    permission_required = ['Portfolio.change_experience',
                           'Portfolio.change_education',
                           'Portfolio.change_skill',
                           'Portfolio.change_certificate']
    permission_denied_message = 'You do not have to Add or Change Experience, Education, Certificate and Skills'

    def get(self, request, *args, **kwargs):
        extracted_data = str.capitalize(request.path.replace('/', ' ')).strip().split(' ')
        model = eval(extracted_data[0].capitalize())
        if len(extracted_data) > 1:
            operation = extracted_data[1]
            pk = int(extracted_data[2])
            if operation == 'delete':
                model.objects.get(pk=pk).delete()
                messages.success(request, f'{model} has been deleted')
        objects = model.objects.filter(portfolio=request.user.portfolio)
        form = eval(f'{extracted_data[0].capitalize()}Form')
        update_forms = {obj.id: form(instance=obj) for obj in objects}
        context = {'portfolio': request.user.portfolio,
                   'form': form,
                   'update_forms': update_forms,
                   'template': extracted_data[0],
                   'url': f'/{extracted_data[0]}',
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
            pk = int(extracted_data[2])
            instance = model.objects.get(pk=pk)
            form = form(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
        return redirect(reverse_lazy(f'Portfolio:{extracted_data[0]}'))
