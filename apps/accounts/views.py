from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.

# Metodo usado para loguear a un usuario
def user_login(request):
    # Si ya esta logueado pase al dashboard
    if request.user.is_authenticated():
        return HttpResponseRedirect('/dashboard')
    else:
        # Si recibe datos mediante post comienza el proceso de logueo
        if request.method =='POST':
            username = request.POST.get('user')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
    
            # Si la cuenta existe se carga con los credenciales
            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.session["id"] = user.id
                    return HttpResponseRedirect('/dashboard')
                else:
                    return render(request,'accounts/login.html', {'error':True})
            else: # Si no se encuentra envia un mensaje de error
                return render(request,'accounts/login.html', {'error':True})
        else: # Si no a enviado datos por post se muestra la pagina de login
            return render(request,'accounts/login.html', {})


# Metodo usado para salir de la cuenta
def user_logout(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect('/account/login')
    else:
        return render(request, 'init/index.html')


# Metodo uasdo para crear un usuario nuevo
def signup(request):
    if request.user.is_authenticated(): # Si ya esta logueado va al dashboard
        return HttpResponseRedirect('/dashboard')
    elif request.method =='POST': # Si se envian datos por POST se procesan para crear la cuenta
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
    else: # Si no a enviado datos por post se muestra la pagina de sign up
        return render(request, 'accounts/signup.html')


# Metodo usado para mostar o modificar los datos del usuario
def account(request):
    if request.user.is_authenticated(): # Si el usuario esta logueado
        if request.method == 'POST':
            if request.POST.get('dis') == 'true':
                request.user.is_active = False
                request.user.save()
                return HttpResponseRedirect('/account/logout')
            else:
                # Se capturan los datos del POST
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
    else: # Si no esta logueado se muestra la pagina de login
        return HttpResponseRedirect('/account/login')