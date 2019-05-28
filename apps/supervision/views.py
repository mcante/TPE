from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


from .models import Movimiento, TipoMovimiento
from .forms import MovimientoForm

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