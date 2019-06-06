from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


from .models import Movimiento, TipoMovimiento, Entrada, DetalleDepuracion
from .forms import MovimientoForm, EntradaForm, DetalleDepuracionForm


""" Movimientos Solicitudes / Devoluciones """
class MovimientoListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"Tecnicos"]
    model = Movimiento
    template_name = 'supervision/movimiento_list.html'

class MovimientoCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"admin", u"Supervisores",]
    model = Movimiento
    form_class = MovimientoForm
    template_name = 'supervision/movimiento_add.html'
    success_url = reverse_lazy('movimiento_list')

class MovimientoUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"admin", u"Supervisores",]
    model = Movimiento
    form_class = MovimientoForm
    template_name = 'supervision/movimiento_add.html'
    success_url = reverse_lazy('movimiento_list')



""" Depuraciones """
class EntradaListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"Tecnicos"]
    model = Entrada
    template_name = 'supervision/entrada_list.html'

    def get_context_data(self, **kwargs):
        context = super(EntradaListView, self).get_context_data(**kwargs)
        context['detalleDepuracion'] = DetalleDepuracion.objects.all()
        return context

class EntradaCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"admin", u"Supervisores",]
    model = Entrada
    form_class = EntradaForm
    template_name = 'supervision/entrada_add.html'

    def get_success_url(self):
        return reverse('entrada_detail', kwargs={'pk':self.object.id})

class EntradaUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"admin", u"Supervisores",]
    model = Entrada
    form_class = EntradaForm
    template_name = 'supervision/entrada_add.html'

    def get_success_url(self):
        return reverse('entrada_detail', kwargs={'pk':self.object.id})
    

class EntradaDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    group_required = [u"admin", u"Supervisores"]
    model = Entrada
    template_name = 'supervision/entrada_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EntradaDetailView, self).get_context_data(**kwargs)
        context['detalle_form'] = DetalleDepuracionForm(initial={'entrada': self.object})
        return context


""" Detalle de Entrada """
class DetalleDepuracionCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"admin", u"Supervisores",]
    model = DetalleDepuracion
    form_class = DetalleDepuracionForm
    template_name = 'supervision/detalle_add.html'

    def get_success_url(self):
        return reverse('entrada_detail', kwargs={'pk':self.object.entrada.id})


class DetalleDepuracionUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"admin", u"Supervisores",]
    model = DetalleDepuracion
    form_class = DetalleDepuracionForm
    template_name = 'supervision/detalle_add.html'

    def get_success_url(self):
        return reverse('entrada_detail', kwargs={'pk':self.object.entrada.id})

# Quitar dipositivo del detalle
class DetalleDeleteView(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = [u"admin", u"Supervisores",]
    model = DetalleDepuracion
    template_name = 'supervision/detalle_delete.html'

    def get_success_url(self):
        return reverse('entrada_detail', kwargs={'pk':self.object.entrada.id})
	