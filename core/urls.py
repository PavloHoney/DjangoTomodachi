from django.db import router
from django.urls import path
from django.urls.conf import include
from .views import index
from .views import listadomanga
from .views import disponibilidad
from .views import nuevomanga
from .views import modificarmanga
from .views import eliminarmanga
from .views import MangaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('manga', MangaViewSet)

urlpatterns = [
    path('', index, name="index"),
    path('listadomanga/', listadomanga, name="listadomanga"),
    path('disponibilidad/', disponibilidad, name="disponibilidad"),
    path('nuevomanga/', nuevomanga, name="nuevomanga"),
    path('modificarmanga/<id>/', modificarmanga, name="modificarmanga"),
    path('eliminarmanga/<id>/', eliminarmanga, name="eliminarmanga"),
    path('api/', include(router.urls)),

]