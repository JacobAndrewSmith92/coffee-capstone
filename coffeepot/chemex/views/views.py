from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class IndexView(TemplateView):

    template_name = 'chemex/index.html'

class TrackerView(TemplateView):

    template_name = 'chemex/coffee_tracker.html'

class FavoriteRoasterView(TemplateView):

    template_name = 'chemex/favorite_roaster.html'

class BrewCalculatorView(TemplateView):

    template_name = 'chemex/brew_calculator.html'

class BrewHistoryView(TemplateView):

    template_name = 'chemex/brew_history.html'