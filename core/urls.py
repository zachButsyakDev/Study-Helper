from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('home/', views.home, name='home'),
    path('account/', views.account, name='account'),
]