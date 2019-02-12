from django.shortcuts import render
from django.views.generic import UpdateView, DetailView, ListView, CreateView
from django.urls import reverse_lazy, reverse

from django.utils.timezone import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from django.contrib.auth.models import User
from .models import Perfil, EquipoCargado, AsignarEquipo, Area, TipoEquipo, Telefono
from apps.evaluaciones.models import Evaluacion
from .forms import PerfilForm, DetalleAsignacionEquipoForm, AsignacionEquipoForm


from django.template import RequestContext

class PerfilUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"admin", u"Tecnicos"]
    model = Perfil
    form_class = PerfilForm
    template_name = 'registration/perfil_update.html'
    success_url = reverse_lazy('home')

class PerfilDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    group_required = [u"admin", u"Tecnicos"]
    model = Perfil
    template_name = 'registration/perfil_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(PerfilDetailView, self).get_context_data(**kwargs)
        hoy = datetime.now()
        
        print("DATOS....")

        # Recorrer los 12 meses del año y agregar al contexto concatenando el mes con su respectivo número.
        # Se filtra por medio del empleado instanciado, el año y mes... pero antes se valida que exista el registro sino da error.
        for i in range(1, 13):
            if( Evaluacion.objects.filter(empleado = self.object.id, fecha__year = hoy.year, fecha__month = i).exists() ):
                context['mes'+ str(i)] = Evaluacion.objects.get(empleado = self.object.id, fecha__year = hoy.year, fecha__month = i).get_total
                print(context['mes'+ str(i)])
        return context

    

class ColaboradoresListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"admin",]
    model = Perfil
    template_name = 'registration/colaboradores_list.html'


# Listar Asignación con su Detalle
class AsignacionEquipoDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    group_required = [u"admin", u"Tecnicos"]
    model = EquipoCargado
    template_name = 'registration/equipo_asignado.html'
    
    def get_context_data(self, **kwargs):
        context = super(AsignacionEquipoDetailView, self).get_context_data(**kwargs)
        context['equipo_form'] = DetalleAsignacionEquipoForm(initial={'asignacion': self.object})
        return context


class ImprimirAsignacionEquipoDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    group_required = [u"admin", u"Tecnicos"]
    model = EquipoCargado
    template_name = 'registration/imprimir_equipo_asignado.html'
    
    def get_context_data(self, **kwargs):
        context = super(ImprimirAsignacionEquipoDetailView, self).get_context_data(**kwargs)
        context['equipo_form'] = DetalleAsignacionEquipoForm(initial={'asignacion': self.object})
        return context



class AsignacionEquipoCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"admin",]
    model = AsignarEquipo
    form_class = AsignacionEquipoForm
    template_name = 'registration/asignar_add.html'

    def get_success_url(self):
        return reverse('equipo_asignado_detail', kwargs={'pk':self.object.asignacion.id})


class AsignacionEquipoUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"admin",]
    model = AsignarEquipo
    form_class = AsignacionEquipoForm
    template_name = 'registration/asignar_add.html'

    def get_success_url(self):
        return reverse('equipo_asignado_detail', kwargs={'pk':self.object.asignacion.id})