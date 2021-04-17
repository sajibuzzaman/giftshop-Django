from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.user_signup,name='user_signup' ),
    path('login/',views.user_login,name='user_login' ),
    path('logout/',views.user_logout,name='user_logout' ),
    path('profile/',views.user_profile,name='user_profile' ),
    path('user_update/',views.user_update,name='user_update' ),
    path('password_update/',views.user_password,name='user_password' ),
    path('user_comment/',views.usercomment,name='usercomment' ),
    path('user_comment_delete/<int:id>/',views.comment_delete, name="comment_delete")

]