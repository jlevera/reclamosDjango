from django.db import models

# Create your models here.
class Inmueble(models.Model):
	def __str__(self):
		return '' + self.nombre
	"""docstring for Inmueble"""
	nombre = models.CharField(max_length=200)
	direccion = models.CharField(max_length=200)
	

