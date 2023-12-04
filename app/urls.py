from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='inicio_app'),
    path('get_users/', views.get_users,name='get_users_app'),
    path('delete_user/', views.delete_user,name='delete_user_app'),

]
