# que es un serializador en django
# bbdd --> datos --> JSON
# JSON --> datos --> bbdd

from rest_framework import fields, serializers
from .models import Manga

class MangaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manga
        fields = ['nombre', 'genero', 'anio', 'tomos', 'editorial', 'sinopsis']