from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('deposit', views.deposit, name="deposit"),
    path('withdraw', views.withdraw, name="withdraw"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('register', views.register, name="register"),
]