from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from .views import MovimientoCreateView, MovimientoUpdateView, MovimientoListView, MovimientoInformeFormView, MovimientoInformeImprimir, \
    EntradaListView, EntradaCreateView, EntradaUpdateView, EntradaDetailView, \
    DetalleDepuracionCreateView, DetalleDepuracionUpdateView, DetalleDeleteView, \
    MovimientoInforme, \
    MovimientoRestList


router = routers.SimpleRouter()
router.register(r'movimientos', MovimientoRestList)


urlpatterns = [
    # MOVIMIENTO
    path('movimiento/add/', MovimientoCreateView.as_view(), name='movimiento_add'),
    path('movimiento/<int:pk>/', MovimientoUpdateView.as_view(), name='movimiento_update'),
    path('movimiento/list/', MovimientoListView.as_view(), name='movimiento_list'),
    path('movimiento/informe/', MovimientoInformeFormView.as_view(), name='movimiento_informe'),
    path('movimiento/informe/print/', MovimientoInformeImprimir.as_view(), name='movimiento_informe_print'),

    # INFORME DE MOVIMIENTOS CON FUNCIONES
    #path('movimiento/informe/json/', MovimientoInforme, name='movimiento_informe_funcion'),

    
    # REST
    path('api/', include(router.urls)),


    # DEPURACION
    path('depuracion/add/', EntradaCreateView.as_view(), name='entrada_add'),
    path('depuracion/<int:pk>/', EntradaUpdateView.as_view(), name='entrada_update'),
    path('depuracion/list/', EntradaListView.as_view(), name='entrada_list'),
    path('depuracion/detail/<int:pk>/', EntradaDetailView.as_view(), name='entrada_detail'),
    path('depuracion/detalle/add/', DetalleDepuracionCreateView.as_view(), name='detalle_add'),
    path('depuracion/detalle/<int:pk>/', DetalleDepuracionUpdateView.as_view(), name='detalle_update'),
    path('depuracion/detalle/quitar/<int:pk>/', DetalleDeleteView.as_view(), name='detalle_delete'),
]
