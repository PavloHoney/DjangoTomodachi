from django.contrib import admin
from .models import Genero, Manga
# Register your models here.

class MangaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'genero', 'anio', 'tomos', 'editorial','sinopsis']
    search_fields = ['nombre', 'genero']
    list_filter = ['genero']
    list_per_page = 10
    
admin.site.register(Genero)
admin.site.register(Manga, MangaAdmin)
