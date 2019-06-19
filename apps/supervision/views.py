from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, FormView
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse, HttpResponse
from django.core import serializers

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


from .models import Movimiento, TipoMovimiento, Entrada, DetalleDepuracion, User
from .forms import MovimientoForm, EntradaForm, DetalleDepuracionForm, MovimientosInformeForm
from .serializers import MovimientoSerializer, MovimientoInformeSerializer, TipoSerializer, UsuariosSerializer
from .filters import MovimientoFilter


from rest_framework import generics

from rest_framework import viewsets

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


class MovimientoInformeFormView(LoginRequiredMixin, FormView):
    """Vista encarga de gestionar el listado de :class:`Proyecto`,obteniendo los datos necesarios
    por medio del metodo GET nos muestra el template proyecto_list.
    """
    model = Movimiento
    form_class = MovimientosInformeForm
    template_name = 'supervision/movimiento_informe.html'

class MovimientoInformeImprimir(LoginRequiredMixin, ListView):
    """Vista encarga de gestionar el listado de :class:`Proyecto`,obteniendo los datos necesarios
    por medio del metodo GET nos muestra el template proyecto_list.
    """
    model = Movimiento
    form_class = MovimientosInformeForm
    template_name = 'supervision/movimiento_informe_imprimir.html'


class MovimientoRestList(viewsets.ModelViewSet):
    serializer_class = MovimientoSerializer
    queryset = Movimiento.objects.all()
    filter_class = MovimientoFilter



""" Generar el Informe de Movimiento -- ESTA FORMA SÓLO FUE UN ENSAYO, NO SE UTILIZARÁ"""
def MovimientoInforme(request):
    if request.is_ajax():
        informe = Movimiento.objects.filter(fecha__range=(request.GET['fecha_min'], request.GET['fecha_max']))
        # Declarar diccionario
        f = []

        # Recorrer el resultado de la consulta e ir generando el diccionario
        for x in informe:

            # Cambiar la palabra True por Completado o False por Pendiente
            if(x.supervision_completada):
                estado = 'Completado'
            else:
                estado = 'Pendiente'
            # Crear para el diccionario
            fila = {'movimiento':x.movimiento,'fecha':x.fecha,'tipo':x.tipo.tipo,'dispositivo':x.dispositivo,'entrega':(x.entrega.first_name + ' ' + x.entrega.last_name),'recibe':(x.recibe.first_name + ' ' + x.recibe.last_name),'kardex':x.kardex,'supervisado':(x.supervisado_por.first_name + ' ' + x.supervisado_por.last_name),'estado':estado}

            # Agregar fila al diccionario
            f.append(fila)

        #response = serializers.serialize('json', informe)
        #return HttpResponse(response, content_type='application/json')

        # Serializar diccionario con safe=False y convertirlo a Json
        return JsonResponse(f, safe=False)
    else:
        return redirect('/')






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
	