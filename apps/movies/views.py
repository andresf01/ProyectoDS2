from django.shortcuts import render
from django.http import HttpResponseRedirect
import json
from urllib2 import *
import tmdbsimple as tmdb # Framework para trabajar con la api
from models import *


tmdb.API_KEY = '513d38be3fea8edcab074553be20034c'


def movie(request, movie_id):
    if request.user.is_authenticated():
        if request.method == 'POST':
            calificacion = request.POST.get('value') # aqui poner extraccion de calificacion
            try:
                ca = request.user.calificacion_set.get(pelicula_id=movie_id)
                ca.calificacion = calificacion
                ca.save()
            except:
                ca = Calificacion(pelicula_id=movie_id, calificacion=calificacion)
                ca.save()
                ca.user.add(request.user)
                ca.save()
            
        print movie_id
        movie = tmdb.Movies(movie_id)
        response = movie.info()
        # print movie.cast
        
        url = Request('http://api.themoviedb.org/3/movie/%s/credits?api_key=%s' %(movie_id, tmdb.API_KEY))
        response_body = urlopen(url).read()
        peliculas = []
        d = json.loads(response_body)

        personajes = []
        for i, j in zip(d['cast'], range(0, 5)):
            array = []
            array.append(i['name'])
            array.append(i['character'])
            personajes.append(array)
            print array
        
        calificacion = 0
        try:
            ca = request.user.calificacion_set.get(pelicula_id=movie_id)
            calificacion = ca.calificacion
        except:
            calificacion = 0
          
        url = Request('http://api.themoviedb.org/3/movie/%s/videos?api_key=%s' %(movie_id, tmdb.API_KEY))
        response_body = urlopen(url).read()
        videos = []
        d = json.loads(response_body)
        videos = d['results']
        trailer = 'https://www.youtube.com/embed/'
        for video in videos:
            if video['site'] == 'YouTube' and video['type'] == 'Trailer':
                trailer += video['key']
                break
        # print trailer
            
        # print type(response)
        # print response
        return render(request, 'movies/movie.html', {'username':request.user.get_username(),
            'movietitle':response['title'], 'poster':response['poster_path'],
            'sinopsis':response['overview'], 'cast':personajes, 'calificacion':calificacion,
            'trailer':trailer
        })
    else:
        return HttpResponseRedirect('/account/login')


def search(request):
    if request.user.is_authenticated():
        if request.method =='GET':
            query = request.GET.get('query')
            if query is not '':
                search = tmdb.Search()
                response = search.movie(query=query)
                movies = []
                print response
                # print type(search.results)
                i = 0
                mov_tmp = []
                for m in response['results']:
                    movie = [m['id'], m['title'], m['poster_path']]
                    mov_tmp.append(movie)
                    i = i + 1
                    if i == 4:
                        movies.append(mov_tmp)
                        mov_tmp = []
                        i = 0
                print movies
                return render(request, 'movies/search.html',
                {'peliculas':movies,
                'username':request.user.get_username(),
                'search':query,
                })
        else:
            return HttpResponseRedirect('/dashboard')
    else:
        return HttpResponseRedirect('/account/login')


def mylist(request):
    if request.user.is_authenticated():
        return render(request, 'movies/list.html', {'username':request.user.get_username()})
    else:
        return render(request, 'accounts/login.html')
        
        
def testApi(request):
    id = 246655
    url = Request('http://api.themoviedb.org/3/movie/%s/credits?api_key=%s' %(id, tmdb.API_KEY))
    response_body = urlopen(url).read()
    d = json.loads(response_body)
    personajes = []
    for i, j in zip(d['cast'], range(0, 5)):
        array = []
        array.append(i['name'])
        array.append(i['character'])
        personajes.append(array)
        print array
    return render(request, 'test_api.html', {'test':d['cast']})