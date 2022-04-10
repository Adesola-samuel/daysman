from django.shortcuts import render, redirect

def index(request):
    #if request.user.is_superuser == 0:
        #return redirect('academy:result')
    return render(request, 'main/index.html', {})
