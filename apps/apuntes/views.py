from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse
import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from .models import Categoria, Nota
from .forms import CategoriaForm, NotaForm
from .serializers import NotaSerializer

from rest_framework import generics

# Categoria
class CategoriaCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"admin", u"Tecnicos"]
    model = Categoria
    form_class = CategoriaForm
    template_name = 'apuntes/categoria_add.html'

    def form_valid(self, form):
        form.instance.creado_por = self.request.user
        return super(CategoriaCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('categoria_detail_notas', kwargs={'pk':self.object.id})


class CategoriaUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"admin", u"Tecnicos"]
    model = Categoria
    form_class = CategoriaForm
    template_name = 'apuntes/categoria_add.html'
    success_url = reverse_lazy('categoria_list')


class CategoriaListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"admin", u"Tecnicos"]
    model = Categoria
    template_name = 'apuntes/categoria_list.html'

    def get_context_data(self, **kwargs):
        context = super(CategoriaListView, self).get_context_data(**kwargs)
        if self.request.user.is_superuser:
            context['categoria'] = Categoria.objects.all()
        else:
            context['categoria'] = Categoria.objects.all().filter(creado_por=self.request.user)
        return context



# Notas
class NotaCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"admin", u"Tecnicos"]
    model = Nota
    form_class = NotaForm
    template_name = 'apuntes/nota_add.html'

    def form_valid(self, form):
        form.instance.creado_por = self.request.user
        print("Usuario:" + str(self.request.user))
        return super(NotaCreateView, self).form_valid(form)
    
    def get_success_url(self):
        print("PK categoria: " + str(self.object.categoria.id))
        return reverse('categoria_detail_notas', kwargs={'pk':self.object.categoria.id})


class NotaUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"admin", u"Tecnicos"]
    model = Nota
    form_class = NotaForm
    template_name = 'apuntes/nota_add.html'
    
    def get_success_url(self):
        return reverse('categoria_detail_notas', kwargs={'pk':self.object.categoria.id})


class NotaListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"admin", u"Tecnicos"]
    model = Nota
    template_name = 'apuntes/nota_list.html'

    def get_context_data(self, **kwargs):
        context = super(NotaListView, self).get_context_data(**kwargs)
        if self.request.user.is_superuser:
            context['notas'] = Nota.objects.all()
        else:
            context['notas'] = Nota.objects.all().filter(creado_por=self.request.user)
        return context


class NotaSeguimientoListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"admin", u"Tecnicos"]
    model = Nota
    template_name = 'apuntes/nota_list.html'

    def get_context_data(self, **kwargs):
        context = super(NotaSeguimientoListView, self).get_context_data(**kwargs)
        if self.request.user.is_superuser:
            context['notas'] = Nota.objects.all().filter(necesita_seguimiento=True)
        else:
            context['notas'] = Nota.objects.all().filter(creado_por=self.request.user, necesita_seguimiento=True)
        return context


class NotaDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    group_required = [u"admin", u"Tecnicos"]
    model = Categoria
    template_name = 'apuntes/categoria_detail_notas.html'

    def get_context_data(self, **kwargs):
        context = super(NotaDetailView, self).get_context_data(**kwargs)
        #context['tabla'] = Nota.objects.all().filter(categoria=self.object).order_by('-fecha') # Ordenar resultado descendentemente por la columna fecha.
        context['nota_form'] = NotaForm(initial={'creado_por': self.request.user, 'categoria':self.object, 'fecha': datetime.datetime.now, 'hora':datetime.datetime.now})
        return context

# Eliminar Nota
class NotaDeleteView(DeleteView):
	model = Nota
	template_name = 'apuntes/nota_delete.html'
	success_url = reverse_lazy('nota_list')

class NotaList(generics.ListCreateAPIView):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer