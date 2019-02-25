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
    
    def __init__(self, *args, **kwargs):
        super(LlamadaAtencionForm, self).__init__(*args, **kwargs)
        self.fields['empleado'].label_from_instance = lambda obj: "%s" % obj.get_full_name()
        self.fields['levantada_por'].label_from_instance = lambda obj: "%s" % obj.get_full_name()