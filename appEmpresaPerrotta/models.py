from django.db import models

# Create your models here.

class Departamento(models.Model):
 nombre = models.CharField(max_length=50)
 telefono = models.IntegerField()

class Empresas_asociadas(models.Model):
 nombre = models.CharField(max_length=50)

class Empleado(models.Model):
 nombre = models.CharField(max_length=40)
 apellido = models.CharField(max_length=40)
 email = models.EmailField ()
 rol = models.CharField(max_length=40)