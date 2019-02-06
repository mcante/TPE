from django import forms

from django.forms import ModelForm
from .models import Version, Evaluacion

class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
        widgets = {
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput()
        }


class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = '__all__'
        widgets = {
            'empleado': forms.Select(attrs={"id":"select2", "tabindex":"1", "class":"primero"}),
            'version': forms.Select(attrs={"id":"select2_1", "tabindex":"2"}),
            'fecha': forms.DateInput(attrs={'class':'myDatepicker2', "tabindex":"3"}),
            'evaluador': forms.Select(attrs={"id":"select2_2", "tabindex":"4"}),
            'penalizado': forms.CheckboxInput(attrs={'class':'switch', "tabindex":"5"}),
            'porcentaje_penalizacion': forms.NumberInput(attrs={"tabindex":"6"}),
            'aspectos_por_mejorar': forms.Textarea(attrs={"tabindex":"7"}),
            'completado': forms.CheckboxInput(attrs={'class':'switch', "tabindex":"8"}),
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput()
        }

class EvaluacionUpdateForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = '__all__'
        widgets = {
            'empleado': forms.Select(attrs={"id":"select2"}),
            'evaluador': forms.Select(attrs={"id":"select2_1"}),
            'penalizado': forms.CheckboxInput(attrs={'class':'switch'}),
            'fecha': forms.DateInput(attrs={'class':'myDatepicker2'}),
            'completado': forms.CheckboxInput(attrs={'class':'switch1'}),
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput(),
            'version': forms.HiddenInput()
        }

