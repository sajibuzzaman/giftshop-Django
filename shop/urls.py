from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('product/<slug:slug>', views.product_details, name='product_details'),
    path('comment/<int:id>', views.CommentView, name='comment'),
]