from django.shortcuts import render
from django.http import HttpResponseRedirect
import tmdbsimple as tmdb # Framework para trabajar con la api


def movie(request):
    if request.user.is_authenticated():
        return render(request, 'movie.html', {'username':request.user.get_username()})
    else:
        return render(request, 'movie.html')
        
def search(request):
    if request.user.is_authenticated():
        if request.method =='GET':
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
            return render(request, 'movies/search.html', {'peliculas':movies, 'username':request.user.get_username(), 'search':query})
        else:
            return HttpResponseRedirect('/dashboard')
    else:
        return HttpResponseRedirect('/dashboard')

def mylist(request):
    if request.user.is_authenticated():
        return render(request, 'movies/list.html', {'username':request.user.get_username()})
    else:
        return render(request, 'accounts/login.html')
        
        
def testApi(request):
    tmdb.API_KEY = '513d38be3fea8edcab074553be20034c'
    search = tmdb.Search()
    response = search.movie(query='batman')
    print response
    return render(request, 'test_api.html', {'test':response})