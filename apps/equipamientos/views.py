from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse
import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from .models import Equipamiento, Informe
from .forms import EquipamientoForm, InformeForm


# EQUIPAMIENTO
class EquipamientoListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"admin", u"Tecnicos"]
    model = Equipamiento
    template_name = 'equipamientos/equipamiento_list.html'


class EquipamientoCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"admin", u"Supervisores"]
    model = Equipamiento
    form_class = EquipamientoForm
    template_name = 'equipamientos/equipamiento_add.html'
    success_url = reverse_lazy('equipamiento_list')

    def form_valid(self, form):
        form.instance.creado_por = self.request.user
        return super(EquipamientoCreateView, self).form_valid(form)


class EquipamientoUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"admin", u"Supervisores"]
    model = Equipamiento
    form_class = EquipamientoForm
    template_name = 'equipamientos/equipamiento_add.html'
    success_url = reverse_lazy('equipamiento_list')





# INFORME DE EQUIPAMIENTO
class InformeListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"admin", u"Tecnicos"]
    model = Informe
    template_name = 'equipamientos/informe_list.html'

class InformeCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"admin", u"Supervisores"]
    model = Informe
    form_class = InformeForm
    template_name = 'equipamientos/informe_add.html'
    success_url = reverse_lazy('informe_list')

    def form_valid(self, form):
        form.instance.creado_por = self.request.user
        return super(InformeCreateView, self).form_valid(form)

class InformeUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"admin", u"Tecnicos"]
    model = Informe
    form_class = InformeForm
    template_name = 'equipamientos/informe_add.html'
    success_url = reverse_lazy('informe_list')

class InformeDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    group_required = [u"admin", u"Tecnicos"]
    model = Informe
    template_name = 'equipamientos/imprimir_informe.html'