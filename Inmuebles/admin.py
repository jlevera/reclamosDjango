from django.contrib import admin

# Register your models here.
from Inmuebles.models import Inmueble
from Reclamos.models import Reclamo

admin.site.register(Inmueble)
admin.site.register(Reclamo)