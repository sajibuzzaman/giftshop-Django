from django.urls import path
from . import views

urlpatterns = [
     path('addingcart/<int:id>/', views.Add_to_Shoping_cart, name='Add_to_Shoping_cart'),
     path('cart_details/', views.cart_details, name='cart_details'),
     path('cart_delete/<int:id>', views.cart_delete, name='cart_delete'),
     path('cart_update/<int:id>', views.cart_update, name='cart_update'),
     path('oder_cart/', views.OrderCart, name='OrderCart'),
    
]