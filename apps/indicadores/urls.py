

from django.urls import path, include

from .views import AsignacionIndicadoresListView, AsignacionIndicadoresUpdateView, AsignacionIndicadoresColaboradorUpdateView, IndicadorListView

urlpatterns = [
    # INDICADORES
    path('list/', AsignacionIndicadoresListView.as_view(), name='indicador_list'),
    path('list/full/', IndicadorListView.as_view(), name='indicador_full_list'),
    path('update/<int:pk>/', AsignacionIndicadoresUpdateView.as_view(), name='indicador_update'),
    path('update/indicador/<int:pk>/', AsignacionIndicadoresColaboradorUpdateView.as_view(), name='indicador_colaborador_update'),
]
