from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.db import IntegrityError
import tmdbsimple as tmdb

def user_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/dashboard')
    else:
        if request.method =='POST':
            username = request.POST.get('user')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
    
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
    elif request.method =='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        exito = True
        try:
            user = User.objects.create_user(username, email, password)
            user = authenticate(username=username, password=password)
            login(request, user)
            request.session["id"] = user.id
            return HttpResponseRedirect('/dashboard')
        except IntegrityError as e:
            return render(request, 'accounts/signup.html', {'error':True})
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
        if request.method == 'POST':
            username = request.user.get_username()
            password = request.POST.get('password')
            change_password = False
            first_name = request.POST.get('firstname')
            last_name = request.POST.get('lastname')
            
            if len(password) > 0:
                request.user.set_password(password)
                change_password = True
            
            request.user.first_name = first_name
            request.user.last_name = last_name
            
            request.user.save()
            
            if change_password:
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        request.session["id"] = user.id
            
            user_data = {
                'username':request.user.get_username(),
                'email':request.user.email,
                'firstname':request.user.first_name,
                'lastname':request.user.last_name,
                'success':True
            }
            return render(request, 'accounts/account.html', user_data)
        else:
            user_data = {
                'username':request.user.get_username(),
                'email':request.user.email,
                'firstname':request.user.first_name,
                'lastname':request.user.last_name
            }
            
            return render(request, 'accounts/account.html', user_data)
    else:
        return HttpResponseRedirect('/login')
    
def search(request):
    if request.user.is_authenticated():
        if request.method =='GET':
            # import requests
            # CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
            # KEY = '513d38be3fea8edcab074553be20034c'
            
            # url = CONFIG_PATTERN.format(key=KEY)
            # r = requests.get(url)
            # config = r.json()
            
            # base_url = config['images']['base_url']
            # sizes = config['images']['poster_sizes']
            # """
            #     'sizes' should be sorted in ascending order, so
            #         max_size = sizes[-1]
            #     should get the largest size as well.        
            # """
            # def size_str_to_int(x):
            #     return float("inf") if x == 'original' else int(x[1:])
            # max_size = max(sizes, key=size_str_to_int)
            
            # IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}' 
            # r = requests.get(IMG_PATTERN.format(key=KEY,imdbid='tt0095016'))
            # api_response = r.json()
            
            
            query = request.GET.get('query')
            tmdb.API_KEY = '513d38be3fea8edcab074553be20034c'
            search = tmdb.Search() 
            response = search.movie(query=query)
            movies = []
            # print type(response)
            # print type(search.results)
            for m in response['results']:
                movie = [m['id'], m['title'], m['poster_path']]
                movies.append(movie)
                # print movie
            print response['results']
            return render(request, 'search.html', {'peliculas':movies, 'username':request.user.get_username(), 'search':query})
        else:
            return HttpResponseRedirect('/dashboard')
    else:
        return HttpResponseRedirect('/dashboard')
        # return render(request, 'search.html')

def mylist(request):
    if request.user.is_authenticated():
        return render(request, 'list.html', {'username':request.user.get_username()})
    else:
        return render(request, 'login.html')
        
def testApi(request):
    tmdb.API_KEY = '513d38be3fea8edcab074553be20034c'
    search = tmdb.Search()
    response = search.movie(query='batman')
    print response
    return render(request, 'test_api.html', {'test':response})
    
def index_new(request):
    return render(request, 'init/index_new.html')