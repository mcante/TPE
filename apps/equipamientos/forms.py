from django import forms

from django.forms import ModelForm
from .models import Equipamiento, Aspectos_Evaluados, Cambio_Equipo, Inconvenientes, Producto_Lista, Productos, Productos_Entregados


class EquipamientoForm(forms.ModelForm):
    class Meta:
        model = Equipamiento
        fields = '__all__'
        widgets = {
            'creado_por': forms.HiddenInput()
        }