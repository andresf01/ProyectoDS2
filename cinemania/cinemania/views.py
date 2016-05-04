from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def login(request):
    t = get_template('login.html')
    html = t.render()
    return HttpResponse(html)
    
def signup(request):
    t = get_template('signup.html')
    html = t.render()
    return HttpResponse(html)
    
def hola(request):
    return HttpResponse("hola mundo")