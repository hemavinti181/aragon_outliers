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
    path('state_view', views.state_view, name='state_view'),
    path('state/add', views.state_add, name='state_add'),
    path('state/state_entry', views.state_entry, name='state_entry'),
    path('state/delete', views.state_delete, name='state_delete'),
    path('city_view', views.city_view, name='city_view'),
    path('city/add', views.city_add, name='city_add'),
    path('city/city_entry', views.city_entry, name='city_entry'),
    path('city/delete', views.city_delete, name='city_delete'),
    path('area_view', views.area_view, name='area_view'),
    path('area/add', views.area_add, name='area_add'),
    path('area/area_entry', views.area_entry, name='area_entry'),
    path('area/delete', views.area_delete, name='area_delete'),
]
