from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from chemex.models import Roast
from django.views.generic import TemplateView, CreateView, ListView, FormView
from chemex.forms import UserCreateForm, FavoriteRoast, FavoriteRoaster, FavoriteBrewingMethod
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'chemex/index.html'


class TrackerView(ListView):
    model = Roast
    template_name = 'chemex/coffee_tracker.html'
    context_object_name = 'roast_list'

    def queryset(self):
        return Roast.objects.filter(user=self.request.user)



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


