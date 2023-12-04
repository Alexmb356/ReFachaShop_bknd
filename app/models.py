from django.db import models

# Create your models here.
#La clase Users hereda de la clase Model.
class Users(models.Model):
    
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    edad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=100)
    codigoPostal = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Portada')