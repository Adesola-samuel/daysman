from django.shortcuts import render

def index(request):
    return render(request,'index_.html',{})

def portfolio_details(request):
    return render(request,'portfolio-details.html', {})

def blog_single(request):
    return render(request,'blog-single.html', {})
