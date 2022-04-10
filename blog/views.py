from django.http import HttpResponse
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.shortcuts import get_object_or_404
#from django.contrib.auth.decorators import login_required
#from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from .models import Post,Comment,PostCategory
from .forms import CommentForm, PostForm
from django.core.paginator import Paginator
from django.http import JsonResponse
#from django.forms.models import model_to_dict
#from django.db.models import Q
from datetime import datetime

def index(request, ):
    posts = Post.objects.all().order_by('-created')
    categories=PostCategory.objects.all()
    recentposts = posts[:6]
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog.html', {'posts': posts,'recent_posts': recentposts,'categories':categories})


def blog_detail(request, pk):
    post = Post.objects.get(id=pk)
    categories=PostCategory.objects.all()
    posts = Post.objects.all().order_by('-created')
    recentposts = posts[:6]
    comments = Comment.objects.filter(post=pk, parent__isnull=True)
    context = {'post': post,
               'comments': comments,
               'comment': CommentForm(),
               'recent_posts': recentposts,
               'categories': categories,
               }
    return render(request, 'blog-single.html', context)


def post(request, ):
    if request.method == 'POST':
        form = Post(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'blog-single.html', {'form': form})


def comment(request, ):
    author = request.user
    post = request.POST.get('post_id')
    body = request.POST.get('body')
    comment_ = Comment(author=author, post_id=post, body=body)
    comment_.save()
    now = datetime.now()
    picture=request.user.biodata.profile_pic.url
    data={'author':author.username,'body':body,'created':now,'picture':picture}
    return JsonResponse(data, status=200)


def post_like(request):
    if request.method =='POST':
        user=request.user
        slug=request.POST.get('slug',None)
        post_instance=get_object_or_404(Post, slug=slug)
        if post_instance.likes.filter(id=user.id).exists():
            post_instance.likes.remove(user)
            message= 'You disliked this'
        else:
            post_instance.likes.add(user)
            message= 'You liked this'
        response={'likes_count':post_instance.get_total_likes,'message':message}
    return JsonResponse(response, status=200)


def comment_like(request):
    if request.method =='POST':
        user=request.user
        slug=request.POST.get('slug',None)
        comment_instance=get_object_or_404(Comment, slug=slug)
        if comment_instance.like.filter(id=user.id).exists():
            comment_instance.like.remove(user)
            message= 'You disliked this'
        else:
            comment_instance.like.add(user)
            message= 'You liked this'
        comment_id = comment_instance.id
        response={'likes_count':comment_instance.get_total_likes,'message':message,'comment_id': comment_id}
    return JsonResponse(response, status=200)
