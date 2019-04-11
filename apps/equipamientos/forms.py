from django import forms
from django.utils.translation import ugettext_lazy as _

from django.forms import ModelForm
from .models import Equipamiento, Aspectos_Evaluados, Cambio_Equipo, Inconvenientes, Producto_Lista, Productos, Productos_Entregados, Informe


class EquipamientoForm(forms.ModelForm):
    class Meta:
        model = Equipamiento
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'class':'myDatepicker'}),
            'creado_por': forms.HiddenInput()
        }

class InformeForm(forms.ModelForm):
    class Meta:
        model = Informe
        fields = '__all__'
        labels = {
            'detalle_inconvenientes': _('Detalle de inconvenientes'),
        }
        widgets = {
            'entrega': forms.Select(attrs={"id":"select2", "tabindex":"1"}),
            'fecha_reporte': forms.DateInput(attrs={'class':'myDatepicker', "tabindex":"2"}),
            'tecnico': forms.Select(attrs={"id":"select2_1", "tabindex":"3"}),
            'supervisor': forms.Select(attrs={"id":"select2_2", "tabindex":"4"}),
            'detalle_inconvenientes': forms.Textarea(attrs={"rows":"8", "tabindex":"5"}),
            'informe_general': forms.Textarea(attrs={"rows":"8", "tabindex":"6"}),
            'observacion_supervisor': forms.Textarea(attrs={"rows":"8", "tabindex":"7"}),
            'inconvenientes': forms.CheckboxInput(attrs={'class':'switch1', "tabindex":"8"}),
            'cerrar_informe': forms.CheckboxInput(attrs={'class':'switch1', "tabindex":"9"}),

            'creado_por': forms.HiddenInput(),
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super(InformeForm, self).__init__(*args, **kwargs)
        self.fields['tecnico'].label_from_instance = lambda obj: "%s" % obj.get_full_name()
        self.fields['supervisor'].label_from_instance = lambda obj: "%s" % obj.get_full_name()