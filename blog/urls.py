from django.urls import path
from . import views

app_name='blog'

urlpatterns=[
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('blog_detail/<int:pk>', views.blog_detail, name='blog_detail'),
    path('comment/', views.comment, name='comment'),
    path('post_like/', views.post_like, name='post_like'),
    path('comment_like/', views.comment_like, name='comment_like'),
]
