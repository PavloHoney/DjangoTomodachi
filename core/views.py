from core.forms import MangaForm
from django.shortcuts import redirect, render
from core.models import Manga
from django.contrib.auth.decorators import login_required, permission_required

#rest_framework

from rest_framework import viewsets
from .serializers import MangaSerializer

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def disponibilidad(request):
    return render(request, 'core/disponibilidad.html')

def listadomanga(request):
    mangas = Manga.objects.all()
    data={
        'mangas':mangas
    }
    return render(request, 'core/listadomanga.html', data)

@permission_required('core.add_manga')
def nuevomanga(request):
    data = {
        'form':MangaForm()
    }
    if request.method == 'POST':
        formulario = MangaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']="Manga guardado correctamente"
        data['form'] = formulario    
    return render(request, 'core/nuevomanga.html',data)

@permission_required('core.change_manga')
def modificarmanga(request, id):
    manga = Manga.objects.get(id=id)
    data = {
        'form':MangaForm(instance=manga)
    }
    if request.method == 'POST':
        formulario = MangaForm(data = request.POST, instance=manga)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']="Manga modificado correctamente"
        data['form']=formulario
    return render(request, 'core/modificarmanga.html', data)

@permission_required('core.delete_manga')
def eliminarmanga(request, id):
    manga = Manga.objects.get(id=id)
    manga.delete()
    return redirect(to="listadomanga")

class MangaViewSet(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer