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
    path('coffee_tracker/roaster/add', views.RoasterFormView.as_view(), name='favorite_roaster'),
    path('coffee_tracker/roast/add', views.RoastFormView.as_view(), name='favorite_roast'),
    path('coffee_tracker/method/add', views.BrewingMethodFormView.as_view(), name='favorite_method'),
    path('coffee_tracker/history', views.BrewHistoryView.as_view(), name='brew_history'),
    path('coffee_tracker/favorites/', views.FavoritesView.as_view(), name='my_favorites'),
    path('coffee_tracker/favorites/roast', views.MyFavoriteRoast.as_view(), name='fav_roast_list'),
    path('coffee_tracker/update/roast/<int:pk>', views.UpdateFavoriteRoast, name='update_roast'),
    path('coffee_tracker/delete/roast/<int:pk>', views.DeleteRoast, name='delete_roast'),
    path('coffee_tracker/favorites/roaster', views.MyFavoriteRoaster.as_view(), name='fav_roaster_list'),
    path('coffee_tracker/update/roaster/<int:pk>', views.UpdateFavoriteRoaster, name='update_roaster'),
    path('coffee_tracker/delete/roaster/<int:pk>', views.DeleteRoaster, name='delete_roaster'),
    path('coffee_tracker/favorites/method', views.MyFavoriteMethod.as_view(), name='fav_method_list'),
    path('coffee_tracker/update/method/<int:pk>', views.UpdateFavoriteMethod, name='update_method'),
    path('coffee_tracker/delete/method/<int:pk>', views.DeleteMethod, name='delete_method'),
]