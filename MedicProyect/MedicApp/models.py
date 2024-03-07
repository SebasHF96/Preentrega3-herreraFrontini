from django.db import models

# Create your models here.

class Profesional(models.Model):
    nombre = models.CharField(max_length=60)
    especialidad = models.CharField(max_length=60)
    consultorio = models.IntegerField()
    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    nombre = models.CharField(max_length=60)
    obraSocial = models.CharField(max_length=60)
    historiaClinica = models.CharField(max_length=60)
    def __str__(self):
        return self.nombre

class Sanatorios(models.Model):
    nombre = models.CharField(max_length=60)
    domicilio = models.CharField(max_length=60)
    telefono = models.IntegerField()
    def __str__(self):
        return self.nombre
   