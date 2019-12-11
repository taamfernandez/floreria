from django.shortcuts import render, redirect
from .models import Flor
from .forms import FlorForm

# Create your views here.
def carrito(request):
        lista=request.session.get("carrito","")
        return render(request,"core/carrito.html",{'contenido':lista})

def agregar_carrito(request,id):

        lista=request.session.get("carrito","")
        lista=lista+";"+str(id)
        request.session["carrito"]=lista
        flores=Flor.objects.all()
        return render(request, "core/galeria.html",{'msg':'agrego','lista':flores})

def home(request):
        data = {
               'flores':Flor.objects.all() 
        }
        return render(request, 'core/home.html')

def galeria(request):
        flores=Flor.objects.all()
        return render(request, 'core/galeria.html',{'lista':flores})

def carrito(request):
        return render(request, 'core/carrito.html')

def login(request):
        return render(request, 'core/login.html')

def registrar(request):
        return render(request, 'core/registrar.html')

def listado_flores(request):
        flores = Flor.objects.all()
        data = {
                'flores':flores
        }
        return render(request, 'core/listado_flores.html', data)

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

def eliminar_flor(request, id):
        flores = Flor.objects.get(id=id)
        flores.delete()
        
        return redirect(to="listado-flores")      

