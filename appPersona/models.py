from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=30)
    fechaNacimiento = models.DateField()
    ciudadNacimiento = models.IntegerField()
    ciudadActual = models.IntegerField()
    email = models.EmailField()
    tipoDocumento = (
        ('dni', 'DNI'),
        ('pasaporte', 'Pasaporte'),
        ('otro', 'Otro'),
    )
    numeroDocumento = models.BigIntegerField()