from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from .models import AsignacionIndicadores, Indicador
from .forms import AsignacionIndicadoresUpdateForm, AsignacionIndicadoresColaboradorUpdateForm



class AsignacionIndicadoresListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"admin", u"Tecnicos"]
    model = AsignacionIndicadores
    template_name = 'indicadores/indicadores_seguimiento_list.html'

    def get_context_data(self, **kwargs):
        context = super(AsignacionIndicadoresListView, self).get_context_data(**kwargs)
        context['indicadores'] = AsignacionIndicadores.objects.all().filter(debe_mejorar=True)
        return context


class IndicadorListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"admin", u"Tecnicos"]
    model = Indicador
    template_name = 'indicadores/indicadores_list.html'

class AsignacionIndicadoresUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"admin",]
    model = AsignacionIndicadores
    form_class = AsignacionIndicadoresUpdateForm
    template_name = 'indicadores/indicadores_update.html'
    
    def get_success_url(self):
        return reverse('evaluacion_detalle', kwargs={'pk':self.object.evaluacion.id})

class AsignacionIndicadoresColaboradorUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"admin", u"Tecnicos"]
    model = AsignacionIndicadores
    form_class = AsignacionIndicadoresColaboradorUpdateForm
    template_name = 'indicadores/indicador_colaborador_update.html'
    
    def get_success_url(self):
        return reverse('evaluacion_detalle', kwargs={'pk':self.object.evaluacion.id})



