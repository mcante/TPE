from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from .views import TarimaListView, TarimaUpdateView, TarimaDetailView, HistoricoInformeFormView, TarimaHistoricoRestList, \
    PasilloRestList, PasilloInformeFormView, TarimaRestList, ConsultaQrRest, \
    DespachoTriageListView, RegistrarTriageListView, ControlTriageDetailView, RegistrarTriageCreateView, DespachoTriageCreateView, \
    ConfirmarControlTriageUpdateView, ControlTriageCreateView, ControlTriageListView, ControlTriageCompletarUpdateView, \
    MaquinasListView, MaquinaHistoricoCreateView, MaquinaPerfilDetailView, MaquinaPerfilUpdateView, MaquinaHistoricoUpdateView
    
    
router = routers.SimpleRouter()
router.register(r'historico/tarimas', TarimaHistoricoRestList)
router.register(r'pasillo/tarimas', PasilloRestList)
router.register(r'tarimas/list', TarimaRestList)

urlpatterns = [
    
    # EQUIPAMIENTO
    path('tarima/list/', TarimaListView.as_view(), name='tarima_list'),
    #path('equipamiento/add/', EquipamientoCreateView.as_view(), name='equipamiento_add'),
    path('tarima/update/<int:pk>/', TarimaUpdateView.as_view(), name='tarima_update'),
    path('tarima/detail/<int:pk>/', TarimaDetailView.as_view(), name='tarima_detail'),
    path('tarima/informe/', HistoricoInformeFormView.as_view(), name='tarima_informe'),

    path('api/', include(router.urls)),

    # PASILLOS
    path('pasillo/informe/', PasilloInformeFormView.as_view(), name='pasillo_informe'),

    # DESDE SUNI
    path('tarima/qrs/', ConsultaQrRest.as_view(), name='tarima_qr_list'),

    
    # CONTROL DE TRIAGE
    path('entrega/triage/list/', DespachoTriageListView.as_view(), name='triage_entregados_list'),
    
    path('entrada/detail/<int:pk>/', ControlTriageDetailView.as_view(), name='entrada_triage_detail'),
    path('entrega/add/triage/', RegistrarTriageCreateView.as_view(), name='triage_add'),
    path('entrega/add/salida/triage/', DespachoTriageCreateView.as_view(), name='despachar_triage_add'),
    path('entrega/update/<int:pk>/', ConfirmarControlTriageUpdateView.as_view(), name='entrega_triage_update'),
    
    path('entrada/add/', ControlTriageCreateView.as_view(), name='entrada_triage_add'),
    path('entrada/update/<int:pk>/', ControlTriageCompletarUpdateView.as_view(), name='entrada_triage_update'),
    path('entrada/triage/list/', ControlTriageListView.as_view(), name='entrada_triage_list'),


    # CONTROL DE 
    path('control/maquinaria/list/', MaquinasListView.as_view(), name='maquinaria_list'),
    path('control/maquinaria/add/', MaquinaHistoricoCreateView.as_view(), name='maquinaria_historico_add'),
    path('control/maquinaria/detail/<int:pk>/', MaquinaPerfilDetailView.as_view(), name='maquinaria_detail'),
    path('control/maquinaria/update/<int:pk>/', MaquinaPerfilUpdateView.as_view(), name='reprogramar_servicio_update'),
    path('control/maquinaria/historico/update/<int:pk>/', MaquinaHistoricoUpdateView.as_view(), name='actualizar_info_servicio_update'),

    
]
