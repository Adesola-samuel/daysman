from django.urls import path
from . import views

app_name = 'about'
urlpatterns =[
    path('',views.index, name='home'),
    path('portfolio details/',views.index, name='portfolio-details'),
]