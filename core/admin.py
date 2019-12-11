from django.contrib import admin
from .models import Flor
# Register your models here.

class FlorAdmin(admin.ModelAdmin):
    list_display =['nombre', 'valor', 'descripcion', 'estado', 'stock']
    search_fields = ['nombre']
    list_per_page = 10

admin.site.register(Flor, FlorAdmin)