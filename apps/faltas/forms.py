from django import forms

from django.forms import ModelForm
from .models import LlamadaAtencion

class LlamadaAtencionForm(forms.ModelForm):
    class Meta:
        model = LlamadaAtencion
        fields = '__all__'
        widgets = {
            'empleado': forms.Select(attrs={"id":"select2", "class":"primero"}),
            'fecha': forms.DateInput(attrs={"class":"myDatepicker2"}),
            'motivo': forms.Textarea(attrs={"rows":"6"}),
            'levantada_por': forms.SelectMultiple(attrs={"id":"multiSelect2"}),
            'compromiso': forms.Textarea(attrs={"rows":"6"}),
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput()
        }