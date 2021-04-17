from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('product/<slug:slug>', views.product_details, name='product_details'),
    path('comment/<int:id>', views.CommentView, name='comment'),
    path('favourite/<int:id>', views.FavouriteView, name='favourite'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('wishlist_delete/<int:id>', views.wishlist_delete, name='wishlist_delete'),
]