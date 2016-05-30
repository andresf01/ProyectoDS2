from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'init/index.html')
    
    
def dashboard(request):
    if request.user.is_authenticated():
        return render(request, 'init/dashboard.html', {'username':request.user.get_username()})
    else:
        return HttpResponseRedirect('/account/login')

    
def index_new(request):
    return render(request, 'init/index_new.html')