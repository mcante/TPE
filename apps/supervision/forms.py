from django import forms

from django.forms import ModelForm
from .models import Movimiento, Entrada, DetalleDepuracion


""" Formulario de Movimientos y kardex """
class MovimientoForm(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = '__all__'
        widgets = {
            'tipo': forms.Select(attrs={"id":"select2"}),
            'fecha': forms.DateInput(attrs={'class':'myDatepicker2'}),
            'entrega': forms.Select(attrs={"id":"select2_1"}),
            'recibe': forms.Select(attrs={"id":"select2_2"}),
            'supervisado_por': forms.Select(attrs={"id":"select2_3"}),
            'completado': forms.CheckboxInput(attrs={'class':'switch'}),
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput()
        }
    
    def __init__(self, *args, **kwargs):
        super(MovimientoForm, self).__init__(*args, **kwargs)
        self.fields['entrega'].label_from_instance = lambda obj: "%s" % obj.get_full_name()
        self.fields['recibe'].label_from_instance = lambda obj: "%s" % obj.get_full_name()
        self.fields['supervisado_por'].label_from_instance = lambda obj: "%s" % obj.get_full_name()




class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'class':'myDatepicker2'}),
            'entrega': forms.Select(attrs={"id":"select2_1"}),
            'recibe': forms.Select(attrs={"id":"select2_2"}),
            'supervisado_por': forms.Select(attrs={"id":"select2_3"}),
            'cerrar': forms.CheckboxInput(attrs={'class':'switch'}),
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput()
        }
    
    def __init__(self, *args, **kwargs):
        super(EntradaForm, self).__init__(*args, **kwargs)
        self.fields['entrega'].label_from_instance = lambda obj: "%s" % obj.get_full_name()
        self.fields['recibe'].label_from_instance = lambda obj: "%s" % obj.get_full_name()
        self.fields['supervisado_por'].label_from_instance = lambda obj: "%s" % obj.get_full_name()


class DetalleDepuracionForm(forms.ModelForm):
    class Meta:
        model = DetalleDepuracion
        fields = '__all__'
        widgets = {
            'entrada': forms.HiddenInput(),
        }