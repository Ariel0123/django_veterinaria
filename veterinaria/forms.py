from django import forms
from django.forms import ModelForm

from .models import Mascota, Cita, Cirugia


class DateInput(forms.DateInput):
    input_type = 'date'


class MascotaForm(ModelForm):

    class Meta:
        model = Mascota
        fields = ['foto', 'nombre', 'especie', 'raza', 'sexo', 'color', 'fecha_nacimiento', 'edad', 'peso']
        widgets = {
            'fecha_nacimiento': DateInput(),
        }


class CitaForm(ModelForm):

    class Meta:
        model = Cita
        fields = ['expediente', 'cita_fecha', 'vacunas', 'nota', 'asistencia']
        widgets = {
            'cita_fecha': DateInput(),
        }

class CirugiaForm(ModelForm):

    class Meta:
        model = Cirugia
        fields = ['expediente', 'causa', 'procedimiento', 'nota', 'fecha_programada', 'realizada']
        widgets = {
            'fecha_programada': DateInput(),
        }


        