from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('brew_calculator/', views.BrewCalculatorView.as_view(), name='brew_calculator'),
    path('coffee_tracker/', views.TrackerView.as_view(), name='coffee_tracker'),
    path('coffee_tracker/favorites', views.FavoriteRoasterView.as_view(), name='favorite_roaster'),
    path('coffee_tracker/history', views.BrewHistoryView.as_view(), name='brew_history'),
]