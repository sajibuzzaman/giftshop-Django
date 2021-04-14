from django.urls import path
from . import views

app_name = 'giftshopApp'
urlpatterns = [
    path('', views.home, name='home')
]