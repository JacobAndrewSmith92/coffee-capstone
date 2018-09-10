from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from chemex.models import UserRoast
from django.views.generic import TemplateView, CreateView, ListView, FormView
from chemex.forms import UserCreateForm, FavoriteRoast
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'chemex/index.html'


class TrackerView(TemplateView):
    template_name = 'chemex/coffee_tracker.html'


class FavoriteRoasterView(TemplateView):
    template_name = 'chemex/favorite_roaster.html'


class BrewCalculatorView(TemplateView):
    template_name = 'chemex/brew_calculator.html'


class BrewHistoryView(ListView):

    model = UserRoast

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brew_history'] = UserRoast.objects.all()[:5]
        print(context)
        return context

class RoastFormView(FormView):

    form_class = FavoriteRoast
    success_url = reverse_lazy('coffee_tracker')
    template_name = 'chemex/favoriteroast_form.html'

    def form_valid(self, form):
        form.save()
        return super(RoastFormView, self).form_valid(form)



class SignUpView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sign_up.html'


