from django import forms

from django.forms import ModelForm
from .models import Tarima, HistoricoTarima, Sector, EstadoTarima, Pasillo

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

    """
    contenido = forms.CharField(
        label='Palabra clave',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    """