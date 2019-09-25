from django.db import models
from Inmuebles.models import Inmueble
from datetime import datetime

# Create your models here.
class Reclamo(models.Model):
	def __str__(self):
		return '' + self.pk + self.titulo

	"""docstring for Inmueble"""
	INICIADO ='IN'
	ENPROGRESO = 'PR'
	FINALIZADO = 'FI'
	ESTADO_RECLAMO = [
        (INICIADO, 'Iniciado'),
        (ENPROGRESO, 'EnProgreso'),
        (FINALIZADO, 'Finalizado'),
    ]

	titulo = models.CharField(max_length=200)
	descripcion = models.TextField()
	inmueble = models.ForeignKey(Inmueble ,on_delete=models.CASCADE,blank=True,null=True)
	unidad = models.CharField(max_length=10)
	comentario = models.CharField(max_length=200)
	estado = models.CharField(max_length=2, choices=ESTADO_RECLAMO, default=INICIADO)
	creado = models.DateTimeField(default=datetime.now, blank=True)