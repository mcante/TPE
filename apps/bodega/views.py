from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DetailView, FormView, TemplateView, View
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
import datetime
from django.db.models import Sum

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from .serializers import TarimaHistoricoSerializer, PasilloSerializer, TarimaRestSerializer
from .models import Tarima, HistoricoTarima, Pasillo, ControlTriage, RegistrarTriage, DespachoTriage, \
    MaquinaPerfil, MaquinaHistorico, Maquina
from .forms import TarimaForm, HistoricoForm, PasilloForm, TarimaRestForm, \
    RegistrarTriageForm, DespachoTriageForm, ConfirmarControlTriageForm, ControlTriageForm, ControlTriageCompletarForm, \
    MaquinaHistoricoForm, MaquinaPerfilForm
from .filters import HistoricoFilter, PasilloFilter, TarimaFilter

from rest_framework import generics

from rest_framework import viewsets

import requests

# TARIMA
class TarimaListView2(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"admin", u"Tecnicos"]
    model = Tarima
    template_name = 'bodega/tarima_list.html'

class TarimaUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"admin", u"Bodega"]
    model = Tarima
    form_class = TarimaForm
    template_name = 'bodega/tarima_update.html'
    success_url = reverse_lazy('tarima_list')

    # Asignar el usuario que está actualizando la tarima
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.editado_por = self.request.user
        return super(TarimaUpdateView, self).form_valid(form)


class TarimaDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    group_required = [u"admin", u"Tecnicos", u"Bodega"]
    model = Tarima
    template_name = 'bodega/tarima_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TarimaDetailView, self).get_context_data(**kwargs)
        context['Historico'] = HistoricoTarima.objects.filter(tarima = self.object.id)
        #context['filter'] = HistoricoFilter(self.request.GET, queryset=self.get_queryset())
        return context


class HistoricoInformeFormView(GroupRequiredMixin, LoginRequiredMixin, FormView):
    group_required = [u"admin", u"Tecnicos", u"Bodega"]
    model = HistoricoTarima
    form_class = HistoricoForm
    template_name = 'bodega/historico_informe.html'


class TarimaHistoricoRestList(viewsets.ModelViewSet):
    serializer_class = TarimaHistoricoSerializer
    queryset = HistoricoTarima.objects.all()
    filter_class = HistoricoFilter

class PasilloRestList(viewsets.ModelViewSet):
    serializer_class = PasilloSerializer
    queryset = Pasillo.objects.all()
    filter_class = PasilloFilter

class PasilloInformeFormView(GroupRequiredMixin, LoginRequiredMixin, FormView):
    group_required = [u"admin", u"Tecnicos", u"Bodega"]
    model = Pasillo
    form_class = PasilloForm
    template_name = 'bodega/pasillo_informe.html'

class TarimaRestList(viewsets.ModelViewSet):
    serializer_class = TarimaRestSerializer
    queryset = Tarima.objects.all()
    filter_class = TarimaFilter

class TarimaListView(GroupRequiredMixin, LoginRequiredMixin, FormView):
    group_required = [u"admin", u"Tecnicos", u"Bodega"]
    model = Tarima
    form_class = TarimaRestForm
    template_name = 'bodega/tarima_list.html'


class TarimaQrListView(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    group_required = [u"admin", u"Tecnicos", u"Bodega"]
    template_name = 'bodega/tarima_qr_list.html'

    def ConsultaQrRest(self):
        url = 'https://suni.funsepa.org/i/api/tarima/138/'
        response = requests.get(url)

        if response.status == 200:
            print (response.content)

        
        return True


class ConsultaQrRest(GroupRequiredMixin, LoginRequiredMixin, View):
    group_required = [u"admin", u"Tecnicos", u"Bodega"]
    
    def get(self, request):

        # Obtener el numero de tarima que viene en la URL
        idTarima = request.GET['id']
        
        # Consultar Rest del suni enviándole el número de tarima.
        response = requests.get('https://suni.funsepa.org/i/api/tarima/'+ idTarima +'/?format=json')
        qrtarima = response.json() # Serializar respuesta Rest a Json

        # Devolver los elementos del Rest-SUNI
        return render(request, 'bodega/tarima_qr_list.html', {
            'qrs_util':qrtarima['dispositivos'],
            'qrs_util_cantidad':qrtarima['cantidad_dispositivos'],
            'qrs_repuesto':qrtarima['repuestos'],
            'qrs_repuesto_cantidad':qrtarima['cantidad_repuestos']
            })




# CONTROL DE TRIAGE

class DespachoTriageListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"admin", u"Bodega", u"Tecnicos"]
    model = DespachoTriage
    template_name = 'bodega/entrega_triage_list.html'

class RegistrarTriageListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"admin", u"Bodega", u"Tecnicos"]
    model = RegistrarTriage
    template_name = 'bodega/prueba2.html'

class ControlTriageDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    group_required = [u"admin", u"Tecnicos", u"Bodega"]
    model = ControlTriage
    template_name = 'bodega/control_triage_detail.html'

    # La consulta annotate es equivalente en sql a distinct y por medio de values se logra un group by para poder agrupar tipos de dispositivos y mostrar su total.
    def get_context_data(self, **kwargs):
        context = super(ControlTriageDetailView, self).get_context_data(**kwargs)
        
        context['ingresar_form'] = RegistrarTriageForm(initial={'creado_por': self.request.user, 'no_entrada':self.object})
        context['despachar_form'] = DespachoTriageForm(initial={'entrega': self.request.user, 'no_entrada':self.object})

        context['Ingresados'] = RegistrarTriage.objects.values('dispositivo__dispositivo').annotate(total=Sum('cantidad')).filter(no_entrada_id = self.object.id)
        context['Entregados'] = DespachoTriage.objects.values('dispositivo__dispositivo').annotate(total=Sum('cantidad')).filter(no_entrada_id = self.object.id)
        
        context['Ingresados_detalle'] = RegistrarTriage.objects.filter(no_entrada_id = self.object.id)
        context['Entregados_detalle'] = DespachoTriage.objects.filter(no_entrada_id = self.object.id)

        existencia = [] # Crear lista que almacerá los diccionarios de la existencia.
        if(context['Entregados']): # Verificar que si existan salidas, sino existen entonces la existencia es igual a la entrada y no será necesario recorrer el for
            """
            Se Recorren las entradas y adentro de las entradas las salidas, la idea es que cuando coincida un dispositivo de entrada con una salida, realice
            la resta para entregar la existencia, sino coincide, guardar la existencia el mismo dato de la entrada. 
            El resultado será almacenado en el diccionario y posteriormente se agrega a la lista. 
            """
            
            """
            for entrada in context['Ingresados']:
                for salida in context['Entregados']:
                    if(entrada['dispositivo__dispositivo']==salida['dispositivo__dispositivo']): # Si existe coincidencia con algún dispositivo de entrada y salida
                        diccionario = {'dispositivo__dispositivo':entrada['dispositivo__dispositivo'], 'total':entrada['total']-salida['total']} # Crear elemento para el diccionario
                        existencia.append(diccionario) # Guardar elemento en la lista.
                        break
                    else:
                        diccionario = {'dispositivo__dispositivo': entrada['dispositivo__dispositivo'], 'total':entrada['total']} # Crear elemento para el diccionario
                        existencia.append(diccionario) # Guardar elemento en la lista.
                        break
            context['Existencia'] = existencia # Si había alguna coincidencia, guardar la lista en el contexto para el template.
            return context # Salir devolviendo el contexto.
            """

            for entrada in context['Ingresados']:
                for salida in context['Entregados']:
                    if(entrada['dispositivo__dispositivo']==salida['dispositivo__dispositivo']): # Si existe coincidencia con algún dispositivo de entrada y salida
                        diccionario = {'dispositivo__dispositivo':entrada['dispositivo__dispositivo'], 'total':entrada['total']-salida['total']} # Crear elemento para el diccionario
                        existencia.append(diccionario) # Guardar elemento en la lista.
                        break
            

            tamanio = len(context['Ingresados'])

            for existe in existencia:
                for entrada in context['Ingresados']:
                    #print(entrada['dispositivo__dispositivo'])

                    if(entrada['dispositivo__dispositivo'] != existe['dispositivo__dispositivo']): # Si existe coincidencia con algún dispositivo de entrada y salida
                        print(entrada['dispositivo__dispositivo'])
                    else:
                        """print(entrada['dispositivo__dispositivo'])"""


            context['Existencia'] = existencia # Si había alguna coincidencia, guardar la lista en el contexto para el template.
            return context # Salir devolviendo el contexto.

        else:
            context['Existencia'] = context['Ingresados'] # Sino hay coincidencias, entonces la existencia es igual a la Entrada.
            return context # Salir devolviendo el contexto.
        
        
        
    
        



class RegistrarTriageCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"admin", u"Bodega"]
    model = RegistrarTriage
    form_class = RegistrarTriageForm
    template_name = 'bodega/entrega_triage_add.html'

    def get_success_url(self):
        return reverse('entrada_triage_detail', kwargs={'pk':self.object.no_entrada.id})


class DespachoTriageCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"admin", u"Bodega"]
    model = DespachoTriage
    form_class = DespachoTriageForm
    template_name = 'bodega/entrega_triage_add.html'

    def get_success_url(self):
        return reverse('entrada_triage_detail', kwargs={'pk':self.object.no_entrada.id})


class ConfirmarControlTriageUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"admin", u"Bodega", u"Tecnicos"]
    model = DespachoTriage
    form_class = ConfirmarControlTriageForm
    template_name = 'bodega/entrega_triage_update.html'
    success_url = reverse_lazy('triage_entregados_list')


class ControlTriageCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"admin", u"Bodega"]
    model = ControlTriage
    form_class = ControlTriageForm
    template_name = 'bodega/entrada_triage_add.html'

    def get_success_url(self):
        return reverse('entrada_triage_detail', kwargs={'pk':self.object.id})


class ControlTriageListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"admin", u"Bodega", u"Tecnicos"]
    model = ControlTriage
    template_name = 'bodega/entrada_list.html'


class ControlTriageCompletarUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"admin", u"Bodega", u"Tecnicos"]
    model = ControlTriage
    form_class = ControlTriageCompletarForm
    template_name = 'bodega/entrada_triage_add.html'

    def get_context_data(self, **kwargs):
        context = super(ControlTriageCompletarUpdateView, self).get_context_data(**kwargs)
       
        context['Ingresados'] = RegistrarTriage.objects.values('dispositivo__dispositivo').annotate(total=Sum('cantidad')).filter(no_entrada_id = self.object.id)
        context['Entregados'] = DespachoTriage.objects.values('dispositivo__dispositivo').annotate(total=Sum('cantidad')).filter(no_entrada_id = self.object.id)
       
        existencia = [] # Crear lista que almacerá los diccionarios de la existencia.
        if(context['Entregados']): # Verificar que si existan salidas, sino existen entonces la existencia es igual a la entrada y no será necesario recorrer el for
            """
            Se Recorren las entradas y adentro de las entradas las salidas, la idea es que cuando coincida un dispositivo de entrada con una salida, realice
            la resta para entregar la existencia, sino coincide, guardar la existencia el mismo dato de la entrada. 
            El resultado será almacenado en el diccionario y posteriormente se agrega a la lista. 
            """
            
            for entrada in context['Ingresados']:
                for salida in context['Entregados']:
                    if(entrada['dispositivo__dispositivo']==salida['dispositivo__dispositivo']): # Si existe coincidencia con algún dispositivo de entrada y salida
                        diccionario = {'dispositivo__dispositivo':entrada['dispositivo__dispositivo'], 'total':entrada['total']-salida['total']} # Crear elemento para el diccionario
                        existencia.append(diccionario) # Guardar elemento en la lista.
                        break
                    else:
                        diccionario = {'dispositivo__dispositivo': entrada['dispositivo__dispositivo'], 'total':entrada['total']} # Crear elemento para el diccionario
                        existencia.append(diccionario) # Guardar elemento en la lista.
                        break
            context['Existencia'] = existencia # Si había alguna coincidencia, guardar la lista en el contexto para el template.
            return context # Salir devolviendo el contexto.

        else:
            context['Existencia'] = context['Ingresados'] # Sino hay coincidencias, entonces la existencia es igual a la Entrada.
            return context # Salir devolviendo el contexto.
        

    
    def get_success_url(self):
        return reverse('entrada_triage_detail', kwargs={'pk':self.object.id})




# CONTROL DE MAQUINAS

class MaquinasListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"admin", u"Bodega", u"Tecnicos"]
    model = MaquinaPerfil
    template_name = 'bodega/maquinas_list.html'


class MaquinaPerfilDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    group_required = [u"admin", u"Tecnicos", u"Bodega"]
    model = MaquinaPerfil
    template_name = 'bodega/maquinaria_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MaquinaPerfilDetailView, self).get_context_data(**kwargs)
        context['historico_form'] = MaquinaHistoricoForm(initial={'maquina':self.object})
        return context


class MaquinaHistoricoCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = [u"admin", u"Bodega"]
    model = MaquinaHistorico
    form_class = MaquinaHistoricoForm
    template_name = 'bodega/historico_maquina_add.html'

    def get_success_url(self):
        return reverse('maquinaria_detail', kwargs={'pk':self.object.maquina.id})


class MaquinaPerfilUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"admin", u"Bodega", u"Tecnicos"]
    model = MaquinaPerfil
    form_class = MaquinaPerfilForm
    template_name = 'bodega/reprogramar_servicio_update.html'

    def get_success_url(self):
        return reverse('maquinaria_detail', kwargs={'pk':self.object.id})

class MaquinaHistoricoUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"admin", u"Bodega", u"Tecnicos"]
    model = MaquinaHistorico
    form_class = MaquinaHistoricoForm
    template_name = 'bodega/historico_servicio_update.html'

    def get_success_url(self):
        return reverse('maquinaria_detail', kwargs={'pk':self.object.maquina.id})