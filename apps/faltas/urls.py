

from django.urls import path, include

from .views import LlamadaAtencionListView, LlamadaAtencionCreateView, LlamadaAtencionUpdateView

urlpatterns = [
    path('list/', LlamadaAtencionListView.as_view(), name='faltas_list'),
    path('add/', LlamadaAtencionCreateView.as_view(), name='faltas_add'),
    path('update/<int:pk>', LlamadaAtencionUpdateView.as_view(), name='faltas_update'),
]
