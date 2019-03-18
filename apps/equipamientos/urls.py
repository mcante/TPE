
from django.urls import path, include

from .views import EquipamientoListView, EquipamientoCreateView, EquipamientoUpdateView

urlpatterns = [
    
    # EQUIPAMIENOT
    path('equipamiento/list/', EquipamientoListView.as_view(), name='equipamiento_list'),
    path('equipamiento/add/', EquipamientoCreateView.as_view(), name='equipamiento_add'),
    path('equipamiento/update/<int:pk>/', EquipamientoUpdateView.as_view(), name='equipamiento_update'),

]
