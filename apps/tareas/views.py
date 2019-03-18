from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy, reverse
import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from .models import AnotacionesTarea, Programaciones, Tareas
from .forms import ProgramacionesForm, TareaForm, TareaUpdateForm, NotaTareaForm

# PROGRAMACIONES
class ProgramacionesListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"admin", u"Tecnicos", u"Supervisores"]
    model = Programaciones
    template_name = 'tareas/programaciones_list.html'

    def get_context_data(self, **kwargs):
        context = super(ProgramacionesListView, self).get_context_data(**kwargs) 
        context['cerrados'] = Programaciones.objects.filter(cerrado = True)

        return context


class ProgramacionesPendientesListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"admin", u"Tecnicos", u"Supervisores"]
    model = Programaciones
    template_name = 'tareas/programaciones_pendientes_list.html'

    def get_context_data(self, **kwargs):
        context = super(ProgramacionesPendientesListView, self).get_context_data(**kwargs) 
        context['pendientes'] = Programaciones.objects.filter(cerrado = False)

        return context


class ProgramacionesCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"admin", u"Supervisores"]
    model = Programaciones
    form_class = ProgramacionesForm
    template_name = 'tareas/programacion_add.html'
    success_url = reverse_lazy('programaciones_pendientes_list')

class ProgramacionesUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"admin", u"Supervisores"]
    model = Programaciones
    form_class = ProgramacionesForm
    template_name = 'tareas/programacion_add.html'
    success_url = reverse_lazy('programaciones_pendientes_list')


class ProgramacionesDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    group_required = [u"admin", u"Tecnicos", u"Supervisores"]
    model = Programaciones
    template_name = 'tareas/programacion_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProgramacionesDetailView, self).get_context_data(**kwargs)
        context['tarea_form'] = TareaForm(initial={'creado_por': self.request.user, 'fecha_hora_planificada': datetime.datetime.now, 'programacion': self.object, 'estado':1})
        
        context['contador_tareas'] = Tareas.objects.filter(programacion = self.object.id).count()
        context['por_hacer'] = Tareas.objects.filter(programacion = self.object.id, estado = 1).count()
        context['haciendo'] = Tareas.objects.filter(programacion = self.object.id, estado = 2).count()
        context['terminadas'] = Tareas.objects.filter(programacion = self.object.id, estado = 3).count()
        context['canceladas'] = Tareas.objects.filter(programacion = self.object.id, estado = 4).count()

        return context




# TAREAS
class TareasListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"admin", u"Tecnicos", u"Supervisores"]
    model = Tareas
    template_name = 'tareas/tareas_list.html'

class TareasCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"admin", u"Tecnicos", u"Supervisores"]
    model = Tareas
    form_class = TareaForm
    template_name = 'tareas/tarea_add.html'
    success_url = reverse_lazy('tareas_list')

    def get_success_url(self):
        return reverse('programacion_detail', kwargs={'pk':self.object.programacion.id})

class TareasUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"admin", u"Tecnicos", u"Supervisores"]
    model = Tareas
    form_class = TareaUpdateForm
    template_name = 'tareas/tarea_add.html'
    success_url = reverse_lazy('tareas_list')

    def get_success_url(self):
        return reverse('tarea_detail', kwargs={'pk':self.object.id})

class TareaDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    group_required = [u"admin", u"Tecnicos", u"Supervisores"]
    model = Tareas
    template_name = 'tareas/tarea_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TareaDetailView, self).get_context_data(**kwargs)
        context['nota_form'] = NotaTareaForm(initial={'fecha_hora_anotacion': datetime.datetime.now, 'tarea': self.object})
        return context

# Nota Task

class NotaCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"admin", u"Tecnicos", u"Supervisores"]
    model = AnotacionesTarea
    form_class = NotaTareaForm
    template_name = 'tareas/nota_add.html'

    def get_success_url(self):
        return reverse('tarea_detail', kwargs={'pk':self.object.tarea.id})