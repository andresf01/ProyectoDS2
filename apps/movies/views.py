from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import json
from urllib2 import *
import tmdbsimple as tmdb # Framework para trabajar con la api
from models import *


tmdb.API_KEY = '513d38be3fea8edcab074553be20034c'


# Encargado de hacer el render de una pelicula especifica
def movie(request, movie_id):
    if request.user.is_authenticated():
        if request.method == 'POST':
            op = request.POST.get('op')
            if op == 'calificar':
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
                return HttpResponse("ok")
            elif op == 'agregar':
                lista_id = request.POST.get('value')
                lista = request.user.lista_set.get(lista_id=lista_id)
                try:
                    lipe = lista.listapeliculas_set.get(pelicula_id=movie_id)
                    return HttpResponse("ok")
                except:
                    lipe = ListaPeliculas(pelicula_id=movie_id)
                    lipe.save()
                    lipe.lista.add(lista)
                    lipe.save()
                    return HttpResponse("ok")
        # print movie_id
        movie = tmdb.Movies(movie_id) # Retorna los datos de la pelicula
        response = movie.info()

        # Cast de la pelicula
        url = Request('http://api.themoviedb.org/3/movie/%s/credits?api_key=%s' %(movie_id, tmdb.API_KEY))
        response_body = urlopen(url).read()
        peliculas = []
        d = json.loads(response_body)
        personajes = []
        for i, j in zip(d['cast'], range(0, 5)): # Se optienen los primeros 5 personajes
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

        # Trailes de una pelicula especifica
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

        # Saca las listas del usuario
        lista_user = []
        li = request.user.lista_set.all()
        for lista in li:
            lista_user.append([lista.lista_id, lista.name])

        # Verifica si la imagen se encuentra disponible
        url_img = "/static/img/img_no_avaible.png"
        if response['poster_path'] is not None:
            url_img = "http://image.tmdb.org/t/p/w300" + str(response['poster_path'])
            
        # Hace render de la pagina con todos los parametros de entrada
        return render(request, 'movies/movie.html', {'username':request.user.get_username(),
            'movietitle':response['title'], 'releasedate':response['release_date'],
            'poster':url_img, 'sinopsis':response['overview'], 
            'cast':personajes, 'calificacion':calificacion,
            'trailer':trailer, 'lists':lista_user, 'autenticated':True
        })
    else: # Si no esta autenticado
        return HttpResponseRedirect('/account/login')


# Encargado de hacer el render de las busquedas de una pelicula
def search(request):
    if request.user.is_authenticated():
        if request.method =='GET':
            query = request.GET.get('query') # Se obtienen los parametros de la busqueda
            if query is not '':
                search = tmdb.Search()
                response = search.movie(query=query) # Se busca una pelicula en la api
                movies = []
                i = 0
                mov_tmp = []
                for m in response['results']:
                    # url_img = "/static/img/img_no_avaible.png"
                    if m['poster_path'] is not None: # Si no tiene imagen no se muestra
                        url_img = "http://image.tmdb.org/t/p/w300" + str(m['poster_path'])
                        movie = [m['id'], m['title'], url_img]
                        mov_tmp.append(movie)
                        i = i + 1
                        if i == 4:
                            movies.append(mov_tmp)
                            mov_tmp = []
                            i = 0
                # print movies
                # Se hace render de la pagina con todos los parametros de entrada
                return render(request, 'movies/search.html',
                {'peliculas':movies,
                'username':request.user.get_username(),
                'search':query, 'autenticated':True
                })
        else: # Si no tiene una peticion GET
            return HttpResponseRedirect('/dashboard')
    else: # Si no esta autenticado
        return HttpResponseRedirect('/account/login')


# Encargado de hacer el render de las peliculas de un usuario
def mylist(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            op = request.POST.get('op') # Captura la opcion
            value = request.POST.get('value')
            if op == 'create': # Si la opcion es crear una lista
                li = Lista(name=value)
                li.save()
                li.user.add(request.user)
                li.save()
                return HttpResponse(li.lista_id)
            elif op == 'delete': # Si la opcion es borrar una lista
                try:
                    li = Lista.objects.get(lista_id=value)
                    li.delete()
                    return HttpResponse("ok")
                except:
                    print "delete error"
                    return HttpResponse("not ok")
        else:
            lista_user = []
            li = request.user.lista_set.all() # Obtengo las listas de un usuario
            for lista in li:
                lista_user.append([lista.lista_id, lista.name])
            
            # Se hace render de la pagina con todos los parametros de entrada
            return render(request, 'movies/mylists.html', {'username':request.user.get_username(), 
            'lists':lista_user, 'autenticated':True})
    else: # Si no esta autenticado
        return HttpResponseRedirect('/account/login')
    

# Encargado de hacer el render de una lista en especifico
def user_list(request, list_id):
    if request.user.is_authenticated():
        if request.method == 'POST':
            op = request.POST.get('op') # Captura la opcion
            value = request.POST.get('value') # Captura el id de la lista
            if op == 'delete':
                try: # Borra una pelicula de una lista
                    lista = request.user.lista_set.get(lista_id=list_id)
                    pelicula = lista.listapeliculas_set.get(pelicula_id=value)
                    pelicula.delete()
                    return HttpResponse("ok")
                except:
                    return HttpResponse("not ok")
        else:
            try: # Carga la lista de un usuario
                lista = request.user.lista_set.get(lista_id=list_id)
                peliculas = []
                li = lista.listapeliculas_set.all() # Obtiene las peliculas de una lista
                for p in li:
                    movie = tmdb.Movies(p.pelicula_id)
                    response = movie.info()
                    peliculas.append([p.pelicula_id, response['title']])
                return render(request, 'movies/list.html', {'username':request.user.get_username(),
                'list_name':lista.name,
                'peliculas':peliculas,
                'autenticated':True
                })
            except Lista.DoesNotExist as e: # Si no existe la lista
                return HttpResponseRedirect('/movies/mylists')
    else: # Si no esta autenticado
        return HttpResponseRedirect('/account/login')
        
        
# Calavera
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