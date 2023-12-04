from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='inicio_app'),
    path('users/', views.get_users,name='get_users_app'),
    path('create_user/', views.create_user,name='create_user_app'),
    path('delete_user/', views.delete_user,name='delete_user_app'),

]
