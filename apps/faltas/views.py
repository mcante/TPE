from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from .models import LlamadaAtencion
from .forms import LlamadaAtencionForm



class LlamadaAtencionListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"admin", u"Tecnicos"]
    model = LlamadaAtencion
    template_name = 'faltas/LlamadaAtencion_list.html'

class LlamadaAtencionCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"admin",]
    model = LlamadaAtencion
    form_class = LlamadaAtencionForm
    template_name = 'faltas/llamadaAtencion_add.html'
    success_url = reverse_lazy('faltas_list')

class LlamadaAtencionUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"admin",]
    model = LlamadaAtencion
    form_class = LlamadaAtencionForm
    template_name = 'faltas/llamadaAtencion_add.html'
    success_url = reverse_lazy('faltas_list')