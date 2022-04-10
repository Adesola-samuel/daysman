from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserLoginForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from  django.contrib.auth.models import Group
from .models import Biodata
from academy.models import StudentProgress
from django.contrib.auth.models import User, Group

def create_user(request):
    if request.user.is_authenticated:
        return redirect('main:home')
    else:
        context = {}
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                #form.save()
                first_name = request.POST.get('first_name')
                last_name= request.POST.get('last_name')
                username= request.POST.get('username')
                email= request.POST.get('email')
                password = request.POST.get('password1')
                password2= request.POST.get('password2')
                user = User.objects.create(first_name=first_name, last_name=last_name, username=username, email=email, password = password, is_active=False)
                group = Group.objects.get(name='Student')
                user.groups.add(group)
                bio = Biodata.objects.create(user=user, surname=last_name, other_names=first_name)
                StudentProgress.objects.create(user=bio, )
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account Successfully created for ' + username )
                return redirect('user_auth:login')
        else:
            form = CreateUserForm()
        context['form'] = form
        return render(request, "create_user.html", context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('main:home')
    else:
        if request.method == 'POST':
            form = UserLoginForm(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                f = Biodata.objects.filter(user = request.user)
                if f.count()>0:
                    return redirect('main:home')
                else:
                    bio = Biodata(user=request.user,surname=request.user.last_name, other_names=request.user.first_name)
                    bio.save()
                    pro = StudentProgress(user=request.user,)
                    pro.save()
                    return redirect('main:home')
            else:
                context = {}
                context['form'] = UserLoginForm()
                messages.info(request, 'username or password is incorrect')
                return render(request, "login.html", context)

        context = {}
        context['form']=UserLoginForm()
        return render(request, "login.html", context)

def user_logout(request):
    logout(request,)
    return redirect('user_auth:login')

