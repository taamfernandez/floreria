from django.urls import path, include
from .views import home, galeria, login, registrar, listado_flores, nueva_flor, modificar_flores, eliminar_flor, agregar_carrito, carrito

urlpatterns = [
    path('', home,name='home'),
    path('galeria/', galeria,name='galeria'),
    path('carrito/', carrito,name='carrito'),
    path('login/', login,name='login'),
    path('registrar/', registrar,name='registrar'),
    path('listado-flores/', listado_flores,name='listado-flores'),
    path('nueva-flor/', nueva_flor,name='nueva-flor'),
    path('modificar-flores/<id>/', modificar_flores,name='modificar-flores'),
    path('eliminar-flor/<id>/', eliminar_flor,name='eliminar-flor'),
    path('agregar-carrito/<id>/',agregar_carrito,name='agregar-carrito'),
    path('carrito/',carrito,name='carrito'),
]
