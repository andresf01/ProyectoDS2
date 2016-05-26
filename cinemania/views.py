from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/dashboard')
    else:
        if request.method =='POST':
            email = request.POST.get('user')
            password = request.POST.get('password')
            user = authenticate(username=email, password=password)
    
            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.session["id"] = user.id
                    return HttpResponseRedirect('/dashboard')
                else:
                    return render(request,'accounts/login.html', {'error':True})
            else:
                return render(request,'accounts/login.html', {'error':True})
        else:
            return render(request,'accounts/login.html', {})
    
def user_logout(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect('/login')
    else:
        return render(request, 'init/index.html')
    
def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/dashboard')
    else:
        return render(request, 'accounts/signup.html')
    
def index(request):
    return render(request, 'init/index.html')
    
def movie(request):
    if request.user.is_authenticated():
        return render(request, 'movie.html', {'username':request.user.get_username()})
    else:
        return render(request, 'movie.html')
    
def dashboard(request):
    if request.user.is_authenticated():
        return render(request, 'dashboard.html', {'username':request.user.get_username()})
    else:
        return HttpResponseRedirect('/login')

def account(request):
    # return render(request, 'accounts/account.html')
    if request.user.is_authenticated():
        user_data = {
            'username':request.user.get_username(),
            'email':request.user.email,
            'name':request.user.first_name,
            'lastname':request.user.last_name
        }
        return render(request, 'accounts/account.html', user_data)
    else:
        return HttpResponseRedirect('/login')
    
def search(request):
    if request.user.is_authenticated():
        return render(request, 'search.html', {'username':request.user.get_username()})
    else:
        return render(request, 'search.html')

def mylist(request):
    if request.user.is_authenticated():
        return render(request, 'search.html', {'username':request.user.get_username()})
    else:
        return render(request, 'search.html')
    