from django.contrib import admin
from django.urls import path
from.import views
app_name = "aragonapp"
urlpatterns = [
    path('', views.index),
    path('helo', views.helo),
    path('signin', views.sign_in),
    path('signup', views.sign_up),
    path('country_list', views.country_list, name='country_list'),
    path('country_view', views.country_view, name='country_view'),
    path('country_edit', views.country_edit, name='country_edit'),
    path('country/add', views.country_add, name='country_add'),
    path('country/delete', views.country_delete, name='country_delete'),
    path('state_list', views.state_list, name='state_list'),
    path('state_view', views.state_view, name='state_view'),
    path('state_edit', views.state_edit, name='state_edit'),
    path('state/add', views.state_add, name='state_add'),
    path('state/delete', views.state_delete, name='state_delete'),
    path('city_list', views.city_list, name='city_list'),
    path('city_view', views.city_view, name='city_view'),
    path('city_edit', views.city_edit, name='city_edit'),
    path('city/add', views.city_add, name='city_add'),
    path('city/delete', views.city_delete, name='city_delete'),
    path('area_list', views.area_list, name='area_list'),
    path('area_view', views.area_view, name='area_view'),
    path('area_edit', views.area_edit, name='area_edit'),
    path('area/add', views.area_add, name='area_add'),
    path('area/delete', views.area_delete, name='area_delete'),

    path('property_list', views.property_list, name='property_list'),
    path('property_view', views.property_view, name='property_view'),
    path('property_edit', views.property_edit, name='property_edit'),
    path('property/add', views.property_add, name='property_add'),
    path('property/delete', views.property_delete, name='property_delete'),

    path('users_list', views.users_list, name='users_list'),
    path('users_view', views.users_view, name='users_view'),
    path('users_edit', views.users_edit, name='users_edit'),
    path('users/add', views.users_add, name='users_add'),
    path('users/delete', views.users_delete, name='users_delete'),
]
