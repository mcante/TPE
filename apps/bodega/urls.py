from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from .views import TarimaListView, TarimaUpdateView, TarimaDetailView, HistoricoInformeFormView, TarimaHistoricoRestList, \
    PasilloRestList, PasilloInformeFormView


router = routers.SimpleRouter()
router.register(r'historico/tarimas', TarimaHistoricoRestList)
router.register(r'pasillo/tarimas', PasilloRestList)

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

]
