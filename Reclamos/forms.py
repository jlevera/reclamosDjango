from django import forms

from .models import Reclamo

class ReclamoForm(forms.ModelForm):

    class Meta:
        model = Reclamo
        fields = ('titulo', 'descripcion','inmueble','unidad', 'estado' )