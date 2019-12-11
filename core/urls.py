from django.urls import path, include
from .views import home, galeria, login, listado_flores, nueva_flor, modificar_flores, eliminar_flor, registro_usuario

urlpatterns = [
    path('', home,name='home'),
    path('galeria/', galeria,name='galeria'),
    path('login/', login,name='login'),
    path('listado-flores/', listado_flores,name='listado-flores'),
    path('nueva-flor/', nueva_flor,name='nueva-flor'),
    path('modificar-flores/<id>/', modificar_flores,name='modificar-flores'),
    path('eliminar-flor/<id>/', eliminar_flor,name='eliminar-flor'),
    path('registro/', registro_usuario,name='registro_usuario'),
]
