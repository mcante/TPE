from django.urls import path, include

from .views import ProgramacionesListView, ProgramacionesCreateView, ProgramacionesUpdateView, ProgramacionesDetailView, ProgramacionesPendientesListView, \
    TareasCreateView, TareasListView, TareasUpdateView, TareaDetailView, TareaEstadoUpdateView, \
    NotaCreateView, ImprimirProgramacionDetailView

urlpatterns = [
    # PROGRAMACIONES
    path('programaciones/completadas/list/', ProgramacionesListView.as_view(), name='programaciones_list'),
    path('programaciones/pendientes/list/', ProgramacionesPendientesListView.as_view(), name='programaciones_pendientes_list'),
    path('programacion/add/', ProgramacionesCreateView.as_view(), name='programacion_add'),
    path('programacion/update/<int:pk>/', ProgramacionesUpdateView.as_view(), name='programacion_update'),
    path('programacion/detail/<int:pk>/', ProgramacionesDetailView.as_view(), name='programacion_detail'),
    path('programacion/imprir/<int:pk>/', ImprimirProgramacionDetailView.as_view(), name='programacion_imprimir'),

    # TAREAS
    path('task/list/', TareasListView.as_view(), name='tareas_list'),
    path('task/add/', TareasCreateView.as_view(), name='tarea_add'),
    path('task/update/<int:pk>/', TareasUpdateView.as_view(), name='tarea_update'),
    path('task/update/estado/<int:pk>/', TareaEstadoUpdateView.as_view(), name='tarea_estado_update'),
    path('task/detail/<int:pk>/', TareaDetailView.as_view(), name='tarea_detail'),

    # NOTA
    path('task/nota/add/', NotaCreateView.as_view(), name='nota_task_add'),

]
