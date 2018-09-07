from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from chemex.forms import UserCreateForm, CustomerUserCreationForm
from django.urls import reverse_lazy

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

class SignUpView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sign_up.html'

# class SignUpCustomerView(CreateView):
#     form_class = CustomerUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/sign_up.html'


# class MainView(TemplateView):
#     template_name = 'registration/sign_up.html'
#     success_url = '/'

#     def get(self, request, *args, **kwargs):
#         user_form = UserCreateForm(self.request.GET or None)
#         customer_form = CustomerUserCreationForm(self.request.GET or None)
#         context = self.get_context_data(**kwargs)
#         context['user_form'] = user_form
#         context['customer_form'] = customer_form
#         return self.render_to_response(context)

