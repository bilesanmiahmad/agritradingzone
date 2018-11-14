from django.urls import path
from django.contrib import admin

from control import views
from trades import views as tv


urlpatterns = [
    path('add-product/', views.add_product, name='add-product'),
    path('products/<int:product_id>', views.details, name='prod-details'),
    path('add-crop/', views.add_crop, name='add-crop'),
    path('crops/', views.list_crops, name='crops'),
    path('products/', tv.list_products, name='products'),
    path('crops/<int:crop_id>', views.edit_crop, name='edit-crop'),
    path('crops/<int:crop_id>/delete', views.delete_crop, name='delete-crop')

]
