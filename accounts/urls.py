from django.urls import path
from django.contrib import admin

from accounts import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]

admin.site.site_header = 'Agri Trading Zone Tech'
