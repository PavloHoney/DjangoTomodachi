from django import forms
from django.forms import ModelForm
from .models import Manga

class MangaForm(ModelForm):
    class Meta:
        model = Manga
        fields = ['nombre', 'genero', 'anio', 'tomos', 'editorial', 'sinopsis']