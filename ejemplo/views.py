from django.shortcuts import render, get_object_or_404
from ejemplo.models import Familiar, Mascotas, Vehiculo
from ejemplo.forms import Buscar, FamiliarForm, MascotasForm, VehiculosForm
from django.views import View


def principal(request):
    return render(request, "ejemplo/principal.html")


#Familiares


def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})


class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})


class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})


class ActualizarFamiliar(View):
  form_class = FamiliarForm
  template_name = 'ejemplo/actualizar_familiar.html'
  initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      return render(request, self.template_name, {'form':form,'familiar': familiar})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=familiar)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'familiar': familiar,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})


class BorrarFamiliar(View):
  template_name = 'ejemplo/familiares.html'
    
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      familiar.delete()
      familiar = Familiar.objects.all()
      return render(request, self.template_name, {'lista_familiares': familiar})




#Mascotas

def monstrar_mascotas(request):
  lista_mascotas = Mascotas.objects.all()
  return render(request, "ejemplo/mascotas.html", {"lista_mascotas": lista_mascotas})


class Altamascota(View):

    form_class = MascotasForm
    template_name = 'ejemplo/alta_mascota.html'
    initial = {"nombre":"", "raza":"", "edad":"", "dueño":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito la mascota {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarMascotas(View):
  form_class = MascotasForm
  template_name = 'ejemplo/actualizar_mascota.html'
  initial = {"nombre":"", "raza":"", "edad":"", "dueño":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      mascotas = get_object_or_404(Mascotas, pk=pk)
      form = self.form_class(instance=mascotas)
      return render(request, self.template_name, {'form':form,'Mascotas': mascotas})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      mascotas = get_object_or_404(Mascotas, pk=pk)
      form = self.form_class(request.POST ,instance=mascotas)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito la mascota {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'Mascotas': mascotas,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class BorrarMascota(View):
  template_name = 'ejemplo/mascotas.html'
    
  def get(self, request, pk): 
      mascotas = get_object_or_404(Mascotas, pk=pk)
      mascotas.delete()
      mascotas = Mascotas.objects.all()
      return render(request, self.template_name, {'lista_mascotas': mascotas})     



#Vehiculos

def monstrar_vehiculos(request):
  lista_vehiculos = Vehiculo.objects.all()
  return render(request, "ejemplo/vehiculos.html", {"lista_vehiculos": lista_vehiculos})


class Altavehiculo(View):

    form_class = VehiculosForm
    template_name = 'ejemplo/alta_vehiculo.html'
    initial = {"marca":"", "modelo":"", "año":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el vehiculo {form.cleaned_data.get('modelo')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class Actualizarvehiculo(View):
  form_class = VehiculosForm
  template_name = 'ejemplo/actualizar_vehiculos.html'
  initial = {"marca":"", "marca":"", "año":""}
  
 # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      vehiculos = get_object_or_404(Vehiculo, pk=pk)
      form = self.form_class(instance=vehiculos)
      return render(request, self.template_name, {'form':form,'Vehiculo': vehiculos})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      vehiculos = get_object_or_404(Vehiculo, pk=pk)
      form = self.form_class(request.POST ,instance=vehiculos)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el vehiculo {form.cleaned_data.get('modelo')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'Vehiculo': vehiculos,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class BorrarVehiculo(View):
  template_name = 'ejemplo/vehiculos.html'
    
  def get(self, request, pk): 
      vehiculos = get_object_or_404(Vehiculo, pk=pk)
      vehiculos.delete()
      vehiculos = Vehiculo.objects.all()
      return render(request, self.template_name, {'lista_vehiculos': vehiculos})    





