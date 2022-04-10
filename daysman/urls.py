from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('', include('main.urls'), name='main'),
    path('admin/', admin.site.urls, name='admin'),
    path('academy/', include('academy.urls'), name='academy'),
    path('help/', include('help.urls'), name='help'),
    path('blog/', include('blog.urls'), name='blog'),
    path('user/', include('user_auth.urls'), name='auth'),
    path('about/', include('about.urls'), name='about'),
]


