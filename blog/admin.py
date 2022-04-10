from django.contrib import admin
from .models import Post,Comment,PostCategory

class PostAdmin(admin.ModelAdmin):
    list_display=('title','body',)

class CommentAdmin(admin.ModelAdmin):
    list_display=('post','body')

class PostCategoryAdmin(admin.ModelAdmin):
    list_display=('category',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)