from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('logout/', auth_views.LogoutView.as_view(), name='logged_out'),
    path('brew_calculator/', views.BrewCalculatorView.as_view(), name='brew_calculator'),
    path('coffee_tracker/', views.TrackerView.as_view(), name='coffee_tracker'),
    path('coffee_tracker/roaster/add', views.FavoriteRoasterView.as_view(), name='favorite_roaster'),
    path('coffee_tracker/roast/add', views.RoastFormView.as_view(), name='favorite_roast'),
    path('coffee_tracker/history', views.BrewHistoryView.as_view(), name='brew_history'),

]