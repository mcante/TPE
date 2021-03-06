"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

#import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),

    #path('__debug__/', include(debug_toolbar.urls)),
    
    # Urls de las apps
    path('falta/', include('apps.faltas.urls')),
    path('', include('apps.evaluaciones.urls')),
    path('indicador/', include('apps.indicadores.urls')),
    path('perfil/', include('apps.registration.urls')),
    path('apuntes/', include('apps.apuntes.urls')),
    path('entregas/', include('apps.equipamientos.urls')),
    path('planificacion/', include('apps.tareas.urls')),
    path('supervision/', include('apps.supervision.urls')),
    path('bodega/', include('apps.bodega.urls')),

    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)