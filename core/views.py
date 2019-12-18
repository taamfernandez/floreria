from django.shortcuts import render, redirect
from .models import Flor
from .forms import FlorForm, CustomUserForm
from django.contrib.auth.decorators import login_required, permission_required 
from django.contrib.auth import login, authenticate

#rest_frameworl¿k

from rest_framework import viewsets
from .serializers import FlorSerializer

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, HttpResponseBadRequest

from django.core import serializers
import json
import requests

from fcm_django.models import FCMDevice

# Create your views here.
@csrf_exempt
@require_http_methods(['POST'])
def guardar_token(request):
        body = request.body.decode('utf-8')
        bodyDict = json.loads(body)

        token = bodyDict['token']

        existe = FCMDevice.objects.filter(registration_id = token, active=True)

        if len(existe) > 0:
                return HttpResponseBadRequest(json.dumps({'mensaje':'el token ya existe'}))

        dispositivo = FCMDevice()
        dispositivo.registration_id = token
        dispositivo.active = True

        #solo si el usuario esta autenticado
        if request.user.is_authenticated:
                dispositivo.user = request.user
        
        try: 
                dispositivo.save()
                return HttpResponse(json.dumps({'mensaje':'token guardado'}))
        except:
                return HttpResponseBadRequest(json.dumps({'mensaje':'no se ha podido guardar'}))



def home(request):
        data = {
               'flores':Flor.objects.all() 
        }
        if 'carro' not in request.session:
                request.session['carro'] = []
        
        carro = request.session['carro'] 

        return render(request, 'core/home.html')

def galeria(request):
        flores=Flor.objects.all()
        return render(request, 'core/galeria.html',{'lista':flores})



@permission_required('core.view_flor')
def listado_flores(request):
        response = requests.get('http://localhost:8000/api/flores/')
        flores=response.json()
        data = {
                'flores':flores
        }
        carro = request.session['carro']
        print(carro)
        return render(request, 'core/listado_flores.html', data)

@permission_required('core.add_flor')
def nueva_flor(request):
        data ={
                'form':FlorForm()
        }

        if request.method == 'POST':
                formulario= FlorForm(request.POST, files=request.FILES)
                if formulario.is_valid():
                    formulario.save()


                    data['mensaje'] = "Guardado correctamente"         
        return render(request, 'core/nueva_flor.html', data)


@permission_required('core.change_flor')
def modificar_flores(request, id):
        flores = Flor.objects.get(id=id)
        data ={
                'form':FlorForm(instance=flores)
        }
        if request.method == 'POST':
                formulario= FlorForm(data=request.POST, instance=flores, files=request.FILES)
                if formulario.is_valid():
                       formulario.save()
                       data['mensaje'] = "Modificado correctamente"
                       data['form'] = FlorForm(instance=Flor.objects.get(id=id))   
        return render(request, 'core/modificar_flores.html', data)    

@permission_required('core.delete_flor')
def eliminar_flor(request, id):
        
        requests.delete("http://localhost:8000/api/flores/"+id+"/") 
        
        return redirect(to="listado-flores")      

def registro_usuario(request):
        data ={
                'form':CustomUserForm()
        } 
        if request.method == 'POST':
                formulario = CustomUserForm(request.POST)
                if formulario.is_valid():
                    formulario.save()
                    username = formulario.cleaned_data['username'] 
                    password = formulario.cleaned_data['password1']
                    user = authenticate(username=username, password=password) 
                    login(request, user)
                    return redirect(to='home')

        return render(request, 'registration/registrar.html', data)

         
class FlorViewSet(viewsets.ModelViewSet):
        queryset = Flor.objects.all() 
        serializer_class = FlorSerializer