from django import forms
from django.utils.translation import ugettext_lazy as _

from django.forms import ModelForm
from .models import Programaciones, Tareas, AnotacionesTarea


class ProgramacionesForm(forms.ModelForm):
    class Meta:
        model = Programaciones
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'class':'myDatepicker2', "tabindex":"1"}),
            'mes': forms.Select(attrs={"id":"select2", "tabindex":"2"}),
            'supervisor': forms.Select(attrs={"id":"select2_1", "tabindex":"3", "class":"primero"}),
            'tecnico': forms.Select(attrs={"id":"select2_2", "tabindex":"4"}),
            'cerrado': forms.CheckboxInput(attrs={'class':'switch1', "tabindex":"5"}),
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput()
        }
    
    def __init__(self, *args, **kwargs):
        super(ProgramacionesForm, self).__init__(*args, **kwargs)
        self.fields['supervisor'].label_from_instance = lambda obj: "%s" % obj.get_full_name()
        self.fields['tecnico'].label_from_instance = lambda obj: "%s" % obj.get_full_name()


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tareas
        fields = '__all__'
        labels = {
            'fecha_hora_planificada': _('Fecha hora fin'),
        }
        widgets = {
            'tarea': forms.Textarea(attrs={"rows":"4", "tabindex":"1"}),
            'fecha_hora_inicio': forms.DateTimeInput(attrs={'class':'myDateTimepicker', "tabindex":"2"}),
            'fecha_hora_planificada': forms.DateTimeInput(attrs={'class':'myDateTimepicker2', "tabindex":"3"}),
            
            'anotaciones': forms.Textarea(attrs={"rows":"4", "tabindex":"4"}),
            
            #'estado': forms.Select(attrs={"id":"select2_1", "tabindex":"5"}),
            'estado': forms.HiddenInput(),
            'creado_por': forms.HiddenInput(),
            'programacion': forms.HiddenInput(),
            'completado': forms.HiddenInput(),
            'fecha_hora_completado': forms.HiddenInput(),
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput()
        }


class TareaUpdateForm(forms.ModelForm):
    class Meta:
        model = Tareas
        fields = '__all__'
        widgets = {
            'anotaciones': forms.Textarea(attrs={"rows":"4", "tabindex":"1"}),
            'estado': forms.Select(attrs={"id":"select2_1", "tabindex":"2", "class":"primero"}),


            'programacion': forms.HiddenInput(),
            'tarea': forms.Textarea(attrs={"rows":"2", 'readonly':'readonly'}),
            'fecha_hora_inicio': forms.DateTimeInput(attrs={'readonly':'readonly'}),
            'fecha_hora_planificada': forms.DateTimeInput(attrs={'readonly':'readonly'}),

            'fecha_hora_completado': forms.HiddenInput(),
            'creado_por': forms.HiddenInput(),
            'completado': forms.HiddenInput(),
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput()
        }


class NotaTareaForm(forms.ModelForm):
    class Meta:
        model = AnotacionesTarea
        fields = '__all__'
        widgets = {
            'apunte': forms.Textarea(attrs={"rows":"6", "tabindex":"1"}),
            
            'fecha_hora_anotacion': forms.HiddenInput(),
            'tarea': forms.HiddenInput(),
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput()
        }