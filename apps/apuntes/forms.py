from django import forms

from django.forms import ModelForm
from .models import Categoria, Nota

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'class':'myDatepicker2'}),
            'descripcion': forms.Textarea(attrs={"rows":"4"}),
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput(),
            'creado_por': forms.HiddenInput(),
        }


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = '__all__'
        widgets = {
            'contenido': forms.Textarea(attrs={"rows":"4"}),
            'fecha': forms.DateInput(attrs={'disabled':'disabled'}),
            'fecha_recordatorio': forms.DateInput(attrs={"class":"myDatepicker"}),
            'hora': forms.TimeInput(attrs={'disabled':'disabled'}),
            'necesita_seguimiento': forms.CheckboxInput(attrs={'class':'switch1'}),
            'categoria': forms.HiddenInput(),
            'creado_por': forms.HiddenInput(),
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput()
        }