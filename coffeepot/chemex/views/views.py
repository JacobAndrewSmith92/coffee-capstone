from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView, ListView, FormView, UpdateView
from django.urls import reverse_lazy
from django import template

from chemex.models import Roast, Roaster, BrewingMethod
from chemex.forms import UserCreateForm, FavoriteRoast, FavoriteRoaster, FavoriteBrewingMethod


"""Home page for the application
"""

class IndexView(TemplateView):
    template_name = 'chemex/index.html'

"""Coffee tracker view is the view that a majority of the app takes place. It will help navigate to all your favorites and adding new favorites along the way.
author: jacob smith
"""

class TrackerView(TemplateView):
    template_name = 'chemex/coffee_tracker.html'


"""Favorites Views that will list each favorite for the user. Will save the roast, roaster, and method.
author: jacob smith

"""
class FavoritesView(TemplateView):
    template_name = 'chemex/myfavorites.html'

"""The three methods below list all the roasts that a user has and updating those if they want to.
author: jacob smith
"""

class MyFavoriteRoast(ListView):
    model = Roast
    context_object_name = 'roast_list'
    template_name = 'chemex/favoriteroast_list.html'

    def queryset(self):
        return Roast.objects.filter(user=self.request.user)

def UpdateFavoriteRoast(request, pk):
    roast = get_object_or_404(Roast, pk=pk)
    if request.method == 'POST':
        form = FavoriteRoast(request.POST, instance=roast)
        roast = form.save(commit=False)
        roast.save()
        return redirect('/coffee_tracker/favorites/roast', pk=roast.pk)
    else:
        form = FavoriteRoast(instance=roast)
    return render(request, 'update/roast_update_form.html', {'form': form})

def DeleteRoast(request, pk):
    roast = get_object_or_404(Roast, pk=pk)
    roast.delete()
    return redirect('/coffee_tracker/favorites/roast')

"""The three methods below list all the roasters that a user has and updating those if they want to.
author: jacob smith
"""

class MyFavoriteRoaster(ListView):
    model = Roaster
    context_object_name = 'roaster_list'
    template_name = 'chemex/favoriteroaster_list.html'

    def queryset(self):
        return Roaster.objects.filter(user=self.request.user)

def UpdateFavoriteRoaster(request, pk):
    roaster = get_object_or_404(Roaster, pk=pk)
    if request.method == 'POST':
        form = FavoriteRoaster(request.POST, instance=roaster)
        roaster = form.save(commit=False)
        roaster.save()
        return redirect('/coffee_tracker/favorites/roaster', pk=roaster.pk)
    else:
        form = FavoriteRoaster(instance=roaster)
    return render(request, 'update/roaster_update_form.html', {'form': form})

def DeleteRoaster(request, pk):
    roaster = get_object_or_404(Roaster, pk=pk)
    roaster.delete()
    return redirect('/coffee_tracker/favorites/roaster')


"""The three methods below list all the methods that a user has and updating those if they want to.
author: jacob smith
"""

class MyFavoriteMethod(ListView):
    model = BrewingMethod
    context_object_name = 'brewingMethod_list'
    template_name = 'chemex/favoritemethod_list.html'

    def queryset(self):
        return BrewingMethod.objects.filter(user=self.request.user)

def UpdateFavoriteMethod(request, pk):
    method = get_object_or_404(BrewingMethod, pk=pk)
    if request.method == 'POST':
        form = FavoriteBrewingMethod(request.POST, instance=method)
        method = form.save(commit=False)
        method.save()
        return redirect('/coffee_tracker/favorites/method', pk=method.pk)
    else:
        form = FavoriteBrewingMethod(instance=method)
    return render(request, 'update/method_update_form.html', {'form': form})

def DeleteMethod(request, pk):
    method = get_object_or_404(BrewingMethod, pk=pk)
    method.delete()
    return redirect('/coffee_tracker/favorites/method')

"""









"""
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


register = template.Library()

@register.filter(name='phone_number')
def phone_number(number):
    """
    Convert a 10 character string into (xxx) xxx-xxxx.
    """
    first = number[0:3]
    second = number[3:6]
    third = number[6:10]
    return '(' + first + ')' + ' ' + second + '-' + third


