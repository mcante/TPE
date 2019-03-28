from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


from .models import Version, Evaluacion
from apps.indicadores.models import VersionIndicador
from .forms import VersionForm, EvaluacionForm, EvaluacionUpdateForm, VersionIndicadorForm

# VERSION
class VersionCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"admin",]
    model = Version
    form_class = VersionForm
    template_name = 'evaluaciones/version_add.html'
    success_url = reverse_lazy('version_list')

class VersionUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"admin",]
    model = Version
    form_class = VersionForm
    template_name = 'evaluaciones/version_add.html'
    success_url = reverse_lazy('version_list')

class VersionListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"admin",]
    model = Version
    template_name = 'evaluaciones/version_list.html'

class VersionDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    group_required = [u"admin", u"Supervisores"]
    model = Version
    template_name = 'evaluaciones/version_detail.html'

    def get_context_data(self, **kwargs):
        context = super(VersionDetailView, self).get_context_data(**kwargs)
        context['add_indicador_form'] = VersionIndicadorForm(initial={'version': self.object})
        return context
    
class VersionIndicadorCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"admin",]
    model = VersionIndicador
    form_class = VersionIndicadorForm
    template_name = 'evaluaciones/version_indicador_add.html'

    def get_success_url(self):
        return reverse('version_detail', kwargs={'pk':self.object.version.id})


# EVALUACION
class EvaluacionCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"admin",]
    model = Evaluacion
    form_class = EvaluacionForm
    template_name = 'evaluaciones/evaluacion_add.html'
    success_url = reverse_lazy('evaluacion_list')

class EvaluacionUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"admin",]
    model = Evaluacion
    form_class = EvaluacionUpdateForm
    template_name = 'evaluaciones/evaluacion_update.html'
    success_url = reverse_lazy('evaluacion_list')


class EvaluacionListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"admin", u"Tecnicos"]
    redirect_unauthenticated_users = True
    raise_exception = True
    success_message = "Usuario sin permisos"
    model = Evaluacion
    template_name = 'evaluaciones/evaluacion_list.html'

class EvaluacionPendienteListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"admin", u"Tecnicos"]
    redirect_unauthenticated_users = True
    raise_exception = True
    success_message = "Usuario sin permisos"
    model = Evaluacion
    template_name = 'evaluaciones/evaluacion_pendiente_list.html'

# Listar Pedido con su Detalle
class DetalleDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    group_required = [u"admin", u"Tecnicos"]
    model = Evaluacion
    template_name = 'evaluaciones/evaluacion_detail.html'

class ImprimirDetalleDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    group_required = [u"admin", u"Tecnicos"]
    model = Evaluacion
    template_name = 'evaluaciones/imprimir_evaluacion.html'

class InicioListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"admin", u"Tecnicos"]
    model = Evaluacion
    template_name = 'evaluaciones/home.html'