from django import forms

from django.forms import ModelForm
from .models import Tarima, HistoricoTarima, Sector, EstadoTarima, Pasillo, ControlTriage, RegistrarTriage, DespachoTriage, \
    MaquinaPerfil, MaquinaHistorico

class TarimaForm(forms.ModelForm):
    class Meta:
        model = Tarima
        fields = '__all__'
        widgets = {
            'sector': forms.Select(attrs={"id":"select2", "tabindex":"1", 'class': 'form-control'}),
            'contenido': forms.Textarea({"tabindex":"2", "rows":"2", 'class': 'form-control'}),
            'estado': forms.Select(attrs={"id":"select2_1", "tabindex":"3", 'class': 'form-control'}),
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput(),
            'editado_por': forms.HiddenInput(),
        }

class HistoricoForm(forms.Form):
    """Formulario que Controla los filtros para poder hacer busquedas
    """
    tarima = forms.ModelChoiceField(
        queryset=Tarima.objects.all(),
        label='Tarima',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', "id":"select2",}))
    
    fecha_min = forms.CharField(
        label='Fecha (inicial)',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control myDatepickerConsulta1'}))
    fecha_max = forms.CharField(
        label='Fecha (final)',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control myDatepickerConsulta2'}))

    sector = forms.ModelChoiceField(
        queryset=Sector.objects.all(),
        label='Sector',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', "id":"select2_1",}))
    
    estado = forms.ModelChoiceField(
        queryset=EstadoTarima.objects.all(),
        label='Estado',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', "id":"select2_2",}))

    """
    contenido = forms.CharField(
        label='Palabra clave',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    """
    

class PasilloForm(forms.Form):
    """Formulario que Controla los filtros para poder hacer busquedas
    """
    pasillo = forms.ModelChoiceField(
        queryset=Pasillo.objects.all(),
        label='Pasillos',
        required=True,
        widget=forms.Select(attrs={'class': 'form-control', "id":"select2",}))


class TarimaRestForm(forms.Form):
    """Formulario que Controla los filtros para poder hacer busquedas
    """
    tarima = forms.ModelChoiceField(
        queryset=Tarima.objects.all(),
        label='Tarima',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', "id":"select2",}))

    sector = forms.ModelChoiceField(
        queryset=Sector.objects.all(),
        label='Sector',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', "id":"select2_1",}))
    
    estado = forms.ModelChoiceField(
        queryset=EstadoTarima.objects.all(),
        label='Estado',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', "id":"select2_2",}))



# CONTROL DE TRIAGE

class ControlTriageForm(forms.ModelForm):
    class Meta:
        model = ControlTriage
        fields = '__all__'
        widgets = {
            'no_entrada': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_entrada': forms.DateInput(attrs={'class':'myDatepicker form-control'}),
            'ingresa_como': forms.Select(attrs={"id":"select2", 'class': 'form-control'}),
            
            'completado': forms.HiddenInput(),

            'entrega': forms.HiddenInput(),
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput(),
        }


class ControlTriageCompletarForm(forms.ModelForm):
    class Meta:
        model = ControlTriage
        fields = '__all__'
        widgets = {
            'completado': forms.CheckboxInput(attrs={'class':'switch1 form-control'}),
            'no_entrada': forms.HiddenInput(),
            'fecha_entrada': forms.HiddenInput(),
            'ingresa_como': forms.HiddenInput(),
            'entrega': forms.HiddenInput(),
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput(),
        }



class RegistrarTriageForm(forms.ModelForm):
    class Meta:
        model = RegistrarTriage
        fields = '__all__'
        widgets = {
            'dispositivo': forms.Select(attrs={"id":"select2_1", 'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'a_inventario_de': forms.Select(attrs={"id":"select2_2", 'class': 'form-control'}),

            'fecha_creacion': forms.DateInput(attrs={'class':'myDatepicker form-control'}),
            'rando_inicia': forms.NumberInput(attrs={'class': 'form-control'}),
            'rando_termina': forms.NumberInput(attrs={'class': 'form-control'}),
            
            'no_entrada': forms.HiddenInput(),
            'creado_por': forms.HiddenInput(),

            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput(),
        }




class DespachoTriageForm(forms.ModelForm):
    class Meta:
        model = DespachoTriage
        fields = '__all__'
        widgets = {
            'dispositivo': forms.Select(attrs={"id":"select2_3", 'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'id':'id_cantidad2'}),
            'a_inventario_de': forms.Select(attrs={"id":"select2_4", 'class': 'form-control'}),

            'fecha_entrega': forms.DateInput(attrs={'class':'myDatepicker1 form-control'}),
            'rando_inicia': forms.NumberInput(attrs={'class': 'form-control'}),
            'rando_termina': forms.NumberInput(attrs={'class': 'form-control'}),

            'recibe': forms.Select(attrs={"id":"select2_5", 'class': 'form-control'}),
            
            'no_entrada': forms.HiddenInput(),
            'entrega': forms.HiddenInput(),

            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(DespachoTriageForm, self).__init__(*args, **kwargs)
        self.fields['recibe'].label_from_instance = lambda obj: "%s" % obj.get_full_name()





class ConfirmarControlTriageForm(forms.ModelForm):
    class Meta:
        model = DespachoTriage
        fields = ['no_entrada', 'firma_digital']
        widgets = {
            'firma_digital': forms.CheckboxInput(attrs={'class':'switch1 form-control'}),
            'no_entrada': forms.HiddenInput(),
        }


# CONTROL DE MAQUINARIA

class MaquinaHistoricoForm(forms.ModelForm):
    class Meta:
        model = MaquinaHistorico
        fields = '__all__'
        widgets = {
            'empresa': forms.Select(attrs={"id":"select2_1", 'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class':'myDatepicker form-control'}),
            'trabajo_realizado': forms.Select(attrs={"id":"select2_2", 'class': 'form-control'}),
            'costo': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'recomendaciones': forms.Textarea(attrs={'class': 'form-control'}),
            'tecnico_supervisor': forms.Select(attrs={"id":"select2_3", 'class': 'form-control'}),
            
            'maquina': forms.HiddenInput(),
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput(),
        }

class MaquinaPerfilForm(forms.ModelForm):
    class Meta:
        model = MaquinaPerfil
        fields = '__all__'
        widgets = {
            'servicio_programado': forms.DateInput(attrs={'class':'myDatepicker form-control'}),
            
            'maquina': forms.HiddenInput(),
            'encargado': forms.HiddenInput(),
            'creado': forms.HiddenInput(),
            'actualizado': forms.HiddenInput(),
        }