from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse
import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from .models import Equipamiento
from .forms import EquipamientoForm


# EQUIPAMIENTO
class EquipamientoListView(ListView):
    model = Equipamiento
    template_name = 'equipamientos/equipamiento_list.html'


class EquipamientoCreateView(CreateView):
    model = Equipamiento
    form_class = EquipamientoForm
    template_name = 'equipamientos/equipamiento_add.html'
    success_url = reverse_lazy('equipamiento_list')

    def form_valid(self, form):
        form.instance.creado_por = self.request.user
        return super(EquipamientoCreateView, self).form_valid(form)


class EquipamientoUpdateView(UpdateView):
    model = Equipamiento
    form_class = EquipamientoForm
    template_name = 'equipamientos/equipamiento_add.html'
    success_url = reverse_lazy('equipamiento_list')