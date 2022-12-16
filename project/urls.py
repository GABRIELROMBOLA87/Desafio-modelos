"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejemplo.views import (monstrar_familiares, principal, monstrar_mascotas, monstrar_vehiculos,
                           BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, BorrarFamiliar, Altamascota,
                           ActualizarMascotas, BorrarMascota, Actualizarvehiculo, BorrarVehiculo, Altavehiculo)



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('principal/', principal),
    path('mi-familia/', monstrar_familiares),
    path('mi-mascota/', monstrar_mascotas),
    path('mi-vehiculo/', monstrar_vehiculos),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('mi-mascota/altamascota', Altamascota.as_view()),
    path('mi-mascota/actualizar/<int:pk>', ActualizarMascotas.as_view()),
    path('mi-mascota/borrar/<int:pk>', BorrarMascota.as_view()),
    path('mi-vehiculo/altavehiculo', Altavehiculo.as_view()),
    path('mi-vehiculo/actualizar/<int:pk>', Actualizarvehiculo.as_view()),
    path('mi-vehiculo/borrar/<int:pk>', BorrarVehiculo.as_view()),
    ]
