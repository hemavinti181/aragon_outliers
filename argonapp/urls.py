from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('',views.index),
    path('helo',views.helo),
    path('signin',views.sign_in),
    path('signup',views.sign_up),
    path('edituser/<int:id>/',views.edit_user),
    path('deleteuser/<int:id>/',views.delete_user),
    path('profile',views.profile)
]
