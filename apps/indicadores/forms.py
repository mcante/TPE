from django import forms

from django.forms import ModelForm
from .models import AsignacionIndicadores

class AsignacionIndicadoresUpdateForm(forms.ModelForm):
    class Meta:
        model = AsignacionIndicadores
        fields = '__all__'
        widgets = {
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput()
        }

class AsignacionIndicadoresColaboradorUpdateForm(forms.ModelForm):
    class Meta:
        model = AsignacionIndicadores
        fields = '__all__'
        widgets = {
            'evaluacion': forms.HiddenInput(),
            'indicador': forms.HiddenInput(),
            'calificacion': forms.HiddenInput(),
            'observaciones_encargado': forms.Textarea(attrs={'readonly':'readonly'}),
            'debe_mejorar': forms.HiddenInput(),
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput()
        }