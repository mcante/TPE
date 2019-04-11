
from django.urls import path, include

from .views import EquipamientoListView, EquipamientoCreateView, EquipamientoUpdateView, \
    InformeListView, InformeCreateView, InformeUpdateView, InformeDetailView

urlpatterns = [
    
    # EQUIPAMIENTO
    path('equipamiento/list/', EquipamientoListView.as_view(), name='equipamiento_list'),
    path('equipamiento/add/', EquipamientoCreateView.as_view(), name='equipamiento_add'),
    path('equipamiento/update/<int:pk>/', EquipamientoUpdateView.as_view(), name='equipamiento_update'),


    # INFORME DE EQUIPAMIENTO
    path('informe/list/', InformeListView.as_view(), name='informe_list'),
    path('informe/add/', InformeCreateView.as_view(), name='informe_add'),
    path('informe/update/<int:pk>/', InformeUpdateView.as_view(), name='informe_update'),
    path('informe/print/<int:pk>/', InformeDetailView.as_view(), name='informe_print'),

]
