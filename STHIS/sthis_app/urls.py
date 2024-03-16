from django.contrib import admin
from django.urls import path
from sthis_app import views


urlpatterns= [
    path('register', views.register, name='register'),
    path('', views.home, name='home'),
    path('admindashboard', views.admindashboard, name='admindashboard'),
    path('locationList', views.locationList, name='locationList'),
    path('destination',views.destination, name='destination'),
    path('addLocation', views.addLocation, name="addLocation"),
]