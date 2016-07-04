from django.shortcuts import render
from django.http import HttpResponseRedirect
from urllib2 import *
import json

API_KEY = '513d38be3fea8edcab074553be20034c'

def index(request):
    return render(request, 'init/index.html')
    
    
def dashboard(request):
    if request.user.is_authenticated():
        # Se guardan las peliculas populares en un arreglo
        url = Request('http://api.themoviedb.org/3/movie/popular?api_key=%s' %(API_KEY))
        popular = []
        try:
            response_body = urlopen(url).read()
            d = json.loads(response_body)
            m = d['results']
            for i, j in zip(range(0, 4), m):
                tmp = []
                tmp.append(m[i]['id'])
                tmp.append(m[i]['title'])
                url_img = "/static/img/img_no_avaible.png"
                if m[i]['poster_path'] is not None:
                    url_img = "http://image.tmdb.org/t/p/w300" + str(m[i]['poster_path'])
                tmp.append(url_img)
                # tmp.append(m[i]['poster_path'])
                popular.append(tmp)
                # TODO: write code...
        except:
            print "Error al cargar peliculas populares"
        
        
        # Se guarda los tipos de genero en un arreglo
        mov_gen = []
        url = Request('http://api.themoviedb.org/3/genre/movie/list?api_key=%s' %(API_KEY))
        try:
            response_body = urlopen(url).read()
            d = json.loads(response_body)
            generos = d['genres']
            for genero in generos:
                tmp = []
                tmp.append(genero['name'])
                url = Request('http://api.themoviedb.org/3/genre/%d/movies?api_key=%s' %(genero['id'],API_KEY))
                try:
                    response_body = urlopen(url).read()
                    d = json.loads(response_body)
                    movies = d['results']
                    movies_tmp = []
                    for movie, i in zip(movies, range(0, 4)) :
                        mov_tmp = []
                        mov_tmp.append(movie['id'])
                        mov_tmp.append(movie['title'])
                        url_img = "/static/img/img_no_avaible.png"
                        if movie['poster_path'] is not None:
                            url_img = "http://image.tmdb.org/t/p/w300" + str(movie['poster_path'])
                        # mov_tmp.append(movie['poster_path'])
                        mov_tmp.append(url_img)
                        # print mov_tmp
                        movies_tmp.append(mov_tmp)
                    tmp.append(movies_tmp)
                    mov_gen.append(tmp)
                except:
                    print "Fallo cargando el genero: " + genero['name']
        except:
            print "Fallo cargando los generos"

        return render(request, 'init/dashboard.html', {'username':request.user.get_username(),
            'pelicula':popular,
            'mov_gen':mov_gen,
            'autenticated':True
        })
    else:
        return HttpResponseRedirect('/account/login')
