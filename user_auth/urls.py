from django.urls import path
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('sign up', views.create_user, name='create_user'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
]

