

from django.urls import path, include

from .views import VersionCreateView, VersionListView, VersionUpdateView, \
EvaluacionCreateView, EvaluacionListView, EvaluacionUpdateView, DetalleDetailView, EvaluacionPendienteListView, \
InicioListView, ImprimirDetalleDetailView

urlpatterns = [
    # VERSION
    path('version/list/', VersionListView.as_view(), name='version_list'),
    path('version/add/', VersionCreateView.as_view(), name='version_add'),
    path('version/update/<int:pk>/', VersionUpdateView.as_view(), name='version_update'),

    # EVALUACION
    path('add/', EvaluacionCreateView.as_view(), name='evaluacion_add'),
    path('update/<int:pk>/', EvaluacionUpdateView.as_view(), name='evaluacion_update'),
    path('list/completadas/', EvaluacionListView.as_view(), name='evaluacion_list'),
    path('list/pendientes/', EvaluacionPendienteListView.as_view(), name='evaluacion_pendiente_list'),

    path('detalle/<int:pk>/', DetalleDetailView.as_view(), name='evaluacion_detalle'),
    path('imprimir/<int:pk>/', ImprimirDetalleDetailView.as_view(), name='imprimir_evaluacion_detalle'),
    
    path('', InicioListView.as_view(), name='home'),
]
