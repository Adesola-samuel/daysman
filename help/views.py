from django.shortcuts import render
from .models import Help
from django.db.models import Q


def help(request):
    if request.method=='GET':
        context={}
        query = request.GET.get('q','')
        if query:
            queryset = (Q(task__icontains=query) | Q(howto__icontains=query))
            results = Help.objects.filter(queryset).distinct()
            if results.count() == 0:
                context['no_result'] = 'No result match for this search.'
                return render(request, 'help.html', context)
            else:
                paginator = Paginator(results, 5)
                page = request.GET.get('page')
                results = paginator.get_page(page)
                context['results']= results
                return render(request, 'help.html', context)
        else:
            results = []
            context['results'] = results
            return render(request, 'help.html', context)
    return render(request, 'help.html')



def help_detail(request,pk):
    context = {}
    context['result'] = Help.objects.get(pk=pk)
    return render(request, "help_detail.html", context)
