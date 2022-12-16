from django import forms
from ejemplo.models import Familiar, Mascotas, Vehiculo

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=10, 
    widget=forms.TextInput(attrs={'placeholder': 'Busque algo...'}))

#Formulario para Familiares

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']



#Formulario para Mascotas

class MascotasForm(forms.ModelForm):
  class Meta:
    model = Mascotas
    fields = ['nombre', 'raza', 'edad', 'dueño']


#Formulario para Autos

class VehiculosForm(forms.ModelForm):
  class Meta:
    model = Vehiculo
    fields = ['marca', 'modelo', 'año']