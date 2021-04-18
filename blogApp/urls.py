from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog_details/<int:id>', views.blog_details, name='blog_details',),
    path('blog_comment/<int:id>', views.CommentBlogView, name='blog_comment',),
    path('search/', views.BlogSearchView, name='BlogSearchView'),

]