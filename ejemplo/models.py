from django.db import models


# Familares

class Familiar(models.Model):

    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
        
    def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"

# Mascotas

class Mascotas(models.Model):

    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=200)
    edad = models.IntegerField()
    dueño = models.CharField(max_length=300)

    def __str__(self):
      return f"{self.nombre}, {self.raza}, {self.edad}, {self.dueño}"
      

# Vehiculos
       
class Vehiculo(models.Model):

    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=200)
    año = models.IntegerField()
        
    def __str__(self):
      return f"{self.modelo}, {self.marca}, {self.año}"




