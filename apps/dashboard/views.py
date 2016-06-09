from django.shortcuts import render
from django.http import HttpResponseRedirect
from urllib2 import *
import json


def index(request):
    return render(request, 'init/index.html')
    
    
def dashboard(request):
    if request.user.is_authenticated():
        url = Request('http://api.themoviedb.org/3/movie/popular?api_key=%s' %('513d38be3fea8edcab074553be20034c'))
        response_body = urlopen(url).read()
        popular = []
        d = json.loads(response_body)
        m = d['results']
        print type(m)
        for i, j in zip(range(0, 4), m):
            tmp = []
            tmp.append(m[i]['id'])
            tmp.append(m[i]['title'])
            tmp.append(m[i]['poster_path'])
            popular.append(tmp)
            # TODO: write code...
        
        return render(request, 'init/dashboard.html', {'username':request.user.get_username(),
            'pelicula':popular
        })
    else:
        return HttpResponseRedirect('/account/login')

    
def index_new(request):
    return render(request, 'init/index_new.html')