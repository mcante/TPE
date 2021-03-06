from django import forms

from django.forms import ModelForm
from .models import Version, Evaluacion
from apps.indicadores.models import VersionIndicador

class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
        widgets = {
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput()
        }

class VersionIndicadorForm(forms.ModelForm):
    class Meta:
        model = VersionIndicador
        fields = '__all__'
        widgets = {
            'indicador': forms.Select(attrs={"id":"select2"}),
            'version': forms.HiddenInput(),
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
    
    def __init__(self, *args, **kwargs):
        super(EvaluacionForm, self).__init__(*args, **kwargs)
        self.fields['empleado'].label_from_instance = lambda obj: "%s" % obj.get_full_name()
        self.fields['evaluador'].label_from_instance = lambda obj: "%s" % obj.get_full_name()



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
        
    def __init__(self, *args, **kwargs):
        super(EvaluacionUpdateForm, self).__init__(*args, **kwargs)
        self.fields['empleado'].label_from_instance = lambda obj: "%s" % obj.get_full_name()
        self.fields['evaluador'].label_from_instance = lambda obj: "%s" % obj.get_full_name()

