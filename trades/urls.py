from django.urls import path
from django.contrib import admin

from trades import views
from control import views as cv


urlpatterns = [
    # path('add-product/', views.add_product, name='add-product'),
    path('', views.list_products, name='products'),
    path('<int:product_id>', cv.details, name='prod-details'),
    path('<int:product_id>/close-product', views.close_product, name='close-product'),
    path('bids/', views.get_bids, name='bids'),
    path('all-bids/', views.all_bids, name='all-bids'),
    path('bids/<int:bid_id>/accept/', views.accept_bid, name='accept-bid'),
    path('bids/<int:bid_id>/deny/', views.deny_bid, name='deny-bid'),
    path('bids/<int:bid_id>', views.get_bid, name='bid'),
    path('<int:product_id>/bid', views.add_bid, name='make-bid'),
    path('sales/', views.get_sales, name='sales'),
    path('sales/add', views.add_sale, name='add-sale'),
    path('sales/<int:sale_id>', views.get_sale, name='sale-item')
]
