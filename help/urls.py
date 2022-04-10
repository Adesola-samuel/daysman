from django.urls import path
from . import views

app_name='help_'
urlpatterns = [
    path('', views.help, name='help'),
    path('<int:pk>/help_detail/', views.help_detail, name='help_detail'),
]