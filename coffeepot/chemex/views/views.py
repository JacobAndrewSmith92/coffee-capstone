from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from chemex.models import Roast, Roaster, BrewingMethod
from django.views.generic import TemplateView, CreateView, ListView, FormView
from chemex.forms import UserCreateForm, FavoriteRoast, FavoriteRoaster, FavoriteBrewingMethod
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'chemex/index.html'


class TrackerView(TemplateView):
    template_name = 'chemex/coffee_tracker.html'


"""Favorites Views that will list each favorite for the user. Will save the roast, roaster, and method.
Author: jacob smith

"""
class FavoritesView(TemplateView):
    template_name = 'chemex/myfavorites.html'

class MyFavoriteRoast(ListView):
    model = Roast
    context_object_name = 'roast_list'
    template_name = 'chemex/favoriteroast_list.html'

    def queryset(self):
        return Roast.objects.filter(user=self.request.user)

class MyFavoriteRoaster(ListView):
    model = Roaster
    context_object_name = 'roaster_list'
    template_name = 'chemex/favoriteroaster_list.html'

    def queryset(self):
        return Roaster.objects.filter(user=self.request.user)

class MyFavoriteMethod(ListView):
    model = BrewingMethod
    context_object_name = 'brewingMethod_list'
    template_name = 'chemex/favoritemethod_list.html'

    def queryset(self):
        return BrewingMethod.objects.filter(user=self.request.user)


class BrewCalculatorView(TemplateView):
    template_name = 'chemex/brew_calculator.html'


class BrewHistoryView(ListView):

    model = Roast

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brew_history'] = Roast.objects.all()[:5]
        print(context)
        return context

class RoastFormView(FormView):

    form_class = FavoriteRoast
    success_url = reverse_lazy('coffee_tracker')
    template_name = 'chemex/favoriteroast_form.html'

    def form_valid(self, form):
        f = form.save()
        f.user.add(self.request.user)
        return super(RoastFormView, self).form_valid(form)


class RoasterFormView(FormView):

    form_class = FavoriteRoaster
    success_url = reverse_lazy('coffee_tracker')
    template_name = 'chemex/favoriteroaster_form.html'

    def form_valid(self, form):
        f = form.save()
        f.user.add(self.request.user)
        return super(RoasterFormView, self).form_valid(form)

class BrewingMethodFormView(FormView):

    form_class = FavoriteBrewingMethod
    success_url = reverse_lazy('coffee_tracker')
    template_name = 'chemex/favoritemethod_form.html'


    def form_valid(self, form):
        f = form.save()
        f.user.add(self.request.user)
        return super(BrewingMethodFormView, self).form_valid(form)


class SignUpView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sign_up.html'


