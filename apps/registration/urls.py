

from django.urls import path, include

from django.contrib.auth.models import User

from .views import PerfilUpdateView, PerfilDetailView, ColaboradoresListView, AsignacionEquipoDetailView, \
AsignacionEquipoCreateView, AsignacionEquipoUpdateView, ImprimirAsignacionEquipoDetailView

urlpatterns = [
    # PEFIL
    path('update/<int:pk>/', PerfilUpdateView.as_view(), name='perfil_update'),
    path('detalle/<int:pk>/', PerfilDetailView.as_view(), name='perfil_detail'),

    path('list/', ColaboradoresListView.as_view(), name='colaboradores_list'),

    path('asignacion/detail/<int:pk>/', AsignacionEquipoDetailView.as_view(), name='equipo_asignado_detail'),
    path('asignacion/detail/print/<int:pk>/', ImprimirAsignacionEquipoDetailView.as_view(), name='imprimir_equipo_asignado_detail'),
    path('asignacion/add/', AsignacionEquipoCreateView.as_view(), name='asignacionar_equipo_add'),
    path('asignacion/update/<int:pk>/', AsignacionEquipoUpdateView.as_view(), name='asignacionar_equipo_update'),
]
