from django.urls import path
from django.contrib import admin

from accounts import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_id>/verify/', views.verify, name='verify'),
    path('<int:user_id>/send-link/<str:password_token>/', views.send_password_link, name='send-link'),
    path('<int:user_id>/change-password/', views.change_password, name='change-password'),
]

admin.site.site_header = 'Agri Trading Zone Tech'
