

from django.urls import path, include

from .views import MovimientoCreateView, MovimientoUpdateView, MovimientoListView

urlpatterns = [
    # MOVIMIENTO
    path('movimiento/add/', MovimientoCreateView.as_view(), name='movimiento_add'),
    path('movimiento/<int:pk>/', MovimientoUpdateView.as_view(), name='movimiento_update'),
    path('movimiento/list/', MovimientoListView.as_view(), name='movimiento_list'),
]
