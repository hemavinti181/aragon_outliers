from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('', views.index),
    path('helo', views.helo),
    path('signin', views.sign_in),
    path('signup', views.sign_up),
    path('country_view', views.country_view, name='country_view'),
    path('country/add', views.country_add, name='country_add'),
    path('country/country_entry', views.country_entry, name='country_entry'),
    path('country/delete', views.country_delete, name='country_delete'),
]
