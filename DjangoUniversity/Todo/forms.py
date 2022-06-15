from attr import attrs
from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):

    # asiciamos el modelo con el formulario
    class Meta: #clase meta dice a la clase como comportarse
        model = Tarea
        fields = ['tarea', 'prioridad']

        widgets = {
            'tarea' : forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'prioridad' : forms.TextInput(attrs={
                'class': 'form-control'
            })


        }
