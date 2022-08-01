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
    
    path('amenities_list', views.amenities_list, name='amenities_list'),
    path('amenities_view', views.amenities_view, name='amenities_view'),
    path('amenities_edit', views.amenities_edit, name='amenities_edit'),
    path('amenities/add', views.amenities_add, name='amenities_add'),
    path('amenities/delete', views.amenities_delete, name='amenities_delete'),
    path('nearby_landmark_list', views.nearby_landmark_list, name='nearby_landmark_list'),
    path('nearby_landmark_view', views.nearby_landmark_view, name='nearby_landmark_view'),
    path('nearby_landmark_edit', views.nearby_landmark_edit, name='nearby_landmark_edit'),
    path('nearby_landmark/add', views.nearby_landmark_add, name='nearby_landmark_add'),
    path('nearby_landmark/delete', views.nearby_landmark_delete, name='nearby_landmark_delete'),
    path('package_list', views.package_list, name='package_list'),
    path('package_view', views.package_view, name='package_view'),
    path('package_edit', views.package_edit, name='package_edit'),
    path('package/add', views.package_add, name='package_add'),
    path('package/delete', views.package_delete, name='package_delete'),
    path('property_types/list', views.property_types_list, name='property_types_list'),
    path('property_types_view', views.property_types_view, name='property_types_view'),
    path('property_types_edit', views.property_types_edit, name='property_types_edit'),
    path('property_types/add', views.property_types_add, name='property_types_add'),
    path('property_types/delete', views.property_types_delete, name='property_types_delete'),
    path('property_for/list', views.property_for_list, name='property_for_list'),
    path('property_for_view', views.property_for_view, name='property_for_view'),
    path('property_for_edit', views.property_for_edit, name='property_for_edit'),
    path('property_for/add', views.property_for_add, name='property_for_add'),
    path('property_for/delete', views.property_for_delete, name='property_for_delete'),
]
