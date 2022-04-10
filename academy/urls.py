from django.urls import path
from . import views

app_name='academy'

urlpatterns=[
    path('', views.index, name='index'),
    path('MyResult', views.result, name='result'),
    path('pre_score', views.pre_score, name='pre_score'),
    path('set_score', views.set_score, name='set_score'),
    path('submit_score', views.submit_score, name='submit_score'),
]

