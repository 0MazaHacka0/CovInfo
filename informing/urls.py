from django.urls import path

from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.home, name='home'),
    path('account', views.account, name='account'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.log_out, name='logout'),

    path('vaccination', views.vaccination, name='vaccination')
]
