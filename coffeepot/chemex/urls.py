from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('brew_calculator/', views.BrewCalculatorView.as_view(), name='brew_calculator'),
    path('coffee_tracker/', views.TrackerView.as_view(), name='coffee_tracker'),
    path('coffee_tracker/favorites', views.FavoriteRoasterView.as_view(), name='favorite_roaster'),
    path('coffee_tracker/history', views.BrewHistoryView.as_view(), name='brew_history'),
]