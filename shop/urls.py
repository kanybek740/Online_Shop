from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('cart/', views.cart_list, name='cart_list'),
    path('<int:pk>', views.product_detail, name='product_detail'),
    path('<int:pk>/add/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:pk>', views.delete_from_cart, name = 'delete_from_cart'),
    path('about/', views.about, name='about'),
]