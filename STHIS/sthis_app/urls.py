from django.contrib import admin
from django.urls import path
from sthis_app import views


urlpatterns= [
    path('register', views.register, name='register'),
    path('', views.home, name='home'),

]