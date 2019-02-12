from django import forms

from django.forms import ModelForm
from .models import Perfil, AsignarEquipo


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput(),
            'area': forms.HiddenInput(),
            'incentivo': forms.NumberInput(attrs={'readonly':'readonly'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class':'myDatepicker2'}),
            'fecha_ingreso': forms.DateInput(attrs={'class':'myDatepicker2', 'readonly':'readonly'}),
            'fecha_salida': forms.DateInput(attrs={'class':'myDatepicker2', 'readonly':'readonly'}),
            'activo': forms.HiddenInput(),
            
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput()
        }


class AsignacionEquipoForm(forms.ModelForm):
    class Meta:
        model = AsignarEquipo
        fields = '__all__'
        widgets = {
            'asignacion': forms.HiddenInput(),
            'tipo_equipo': forms.HiddenInput(),
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput()
        }


class DetalleAsignacionEquipoForm(forms.ModelForm):
    class Meta:
        model = AsignarEquipo
        fields = '__all__'
        widgets = {
            'tipo_equipo': forms.Select(attrs={"id":"select2"}),
        	'asignacion': forms.HiddenInput(),
            'devolucion': forms.HiddenInput(),
            'devuelve': forms.HiddenInput(),
            'observaciones': forms.HiddenInput(),
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput()
        }
