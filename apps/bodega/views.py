from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DetailView, FormView, TemplateView, View
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from .serializers import TarimaHistoricoSerializer, PasilloSerializer, TarimaRestSerializer
from .models import Tarima, HistoricoTarima, Pasillo
from .forms import TarimaForm, HistoricoForm, PasilloForm, TarimaRestForm
from .filters import HistoricoFilter, PasilloFilter, TarimaFilter

from rest_framework import generics

from rest_framework import viewsets

import requests

# TARIMA
class TarimaListView2(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"admin", u"Tecnicos"]
    model = Tarima
    template_name = 'bodega/tarima_list.html'

class TarimaUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"admin", u"Bodega"]
    model = Tarima
    form_class = TarimaForm
    template_name = 'bodega/tarima_update.html'
    success_url = reverse_lazy('tarima_list')

    # Asignar el usuario que está actualizando la tarima
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.editado_por = self.request.user
        return super(TarimaUpdateView, self).form_valid(form)


class TarimaDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    group_required = [u"admin", u"Tecnicos", u"Bodega"]
    model = Tarima
    template_name = 'bodega/tarima_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TarimaDetailView, self).get_context_data(**kwargs)
        context['Historico'] = HistoricoTarima.objects.filter(tarima = self.object.id)
        #context['filter'] = HistoricoFilter(self.request.GET, queryset=self.get_queryset())
        return context


class HistoricoInformeFormView(GroupRequiredMixin, LoginRequiredMixin, FormView):
    group_required = [u"admin", u"Tecnicos", u"Bodega"]
    model = HistoricoTarima
    form_class = HistoricoForm
    template_name = 'bodega/historico_informe.html'


class TarimaHistoricoRestList(viewsets.ModelViewSet):
    serializer_class = TarimaHistoricoSerializer
    queryset = HistoricoTarima.objects.all()
    filter_class = HistoricoFilter

class PasilloRestList(viewsets.ModelViewSet):
    serializer_class = PasilloSerializer
    queryset = Pasillo.objects.all()
    filter_class = PasilloFilter

class PasilloInformeFormView(GroupRequiredMixin, LoginRequiredMixin, FormView):
    group_required = [u"admin", u"Tecnicos", u"Bodega"]
    model = Pasillo
    form_class = PasilloForm
    template_name = 'bodega/pasillo_informe.html'

class TarimaRestList(viewsets.ModelViewSet):
    serializer_class = TarimaRestSerializer
    queryset = Tarima.objects.all()
    filter_class = TarimaFilter

class TarimaListView(GroupRequiredMixin, LoginRequiredMixin, FormView):
    group_required = [u"admin", u"Tecnicos", u"Bodega"]
    model = Tarima
    form_class = TarimaRestForm
    template_name = 'bodega/tarima_list.html'


class TarimaQrListView(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    group_required = [u"admin", u"Tecnicos", u"Bodega"]
    template_name = 'bodega/tarima_qr_list.html'

    def ConsultaQrRest(self):
        url = 'https://suni.funsepa.org/i/api/tarima/138/'
        response = requests.get(url)

        if response.status == 200:
            print (response.content)

        
        return True


class ConsultaQrRest(GroupRequiredMixin, LoginRequiredMixin, View):
    group_required = [u"admin", u"Tecnicos", u"Bodega"]
    
    def get(self, request):

        # Obtener el numero de tarima que viene en la URL
        idTarima = request.GET['id']
        
        # Consultar Rest del suni enviándole el número de tarima.
        response = requests.get('https://suni.funsepa.org/i/api/tarima/'+ idTarima +'/?format=json')
        qrtarima = response.json() # Serializar respuesta Rest a Json

        # Devolver los elementos del Rest-SUNI
        return render(request, 'bodega/tarima_qr_list.html', {
            'qrs_util':qrtarima['dispositivos'],
            'qrs_util_cantidad':qrtarima['cantidad_dispositivos'],
            'qrs_repuesto':qrtarima['repuestos'],
            'qrs_repuesto_cantidad':qrtarima['cantidad_repuestos']
            })
