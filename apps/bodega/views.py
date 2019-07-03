from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DetailView, FormView
from django.urls import reverse_lazy, reverse
import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from .serializers import TarimaHistoricoSerializer, PasilloSerializer
from .models import Tarima, HistoricoTarima, Pasillo
from .forms import TarimaForm, HistoricoForm, PasilloForm
from .filters import HistoricoFilter, PasilloFilter

from rest_framework import generics

from rest_framework import viewsets

# TARIMA
class TarimaListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
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