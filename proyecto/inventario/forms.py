from django import forms
from .models import Incidencia

class DateInput(forms.DateInput):
    input_type = 'date'
    
class IncidenciaForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = ('fechaInicio','fechaTermino','responsable','nombre','descripcion')
        widgets = {
            'fechaInicio': DateInput(),
            'fechaTermino': DateInput()
        }
