from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils import timezone
from autoslug import AutoSlugField

class PostCategory(models.Model):
    category=models.CharField(max_length=35)
    def __str__(self):
        return self.category

class Post(models.Model):
    author = models.ForeignKey(User, on_delete =models.CASCADE)
    category = models.ForeignKey(PostCategory, on_delete =models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(null=True, blank=True)
    img = models.ImageField(upload_to='static/blog/images', blank = True,null = True)
    likes = models.ManyToManyField(User, related_name='likes')
    slug= AutoSlugField(populate_from='title',unique_with='created__month')

    @property
    def get_total_likes(self):
        return self.likes.count()
    def publish(self):
        self.published = timezone.now()
        self.save()
    def delete(self, *args, **kwargs):
        self.img.delete()
        super().delete(*args, **kwargs)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='replies', blank=True)
    like= models.ManyToManyField(User, related_name='like',blank=True)
    slug = AutoSlugField(populate_from='body',unique_with='created__month')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return str(self.body)[:30]

    @property
    def get_total_likes(self):
        return self.like.count()  



