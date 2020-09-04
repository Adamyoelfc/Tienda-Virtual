"""TiendaVirtual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from app_tienda import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('cat_alim_ref/', views.alimentos_ref, name='cat_alim_ref'),
    path('cat_alim/', views.alimentos, name='cat_alim'),
    path('cat_utiles_hog/', views.util_hog, name='cat_utiles_hog'),
    path('carr/add/<int:id>/', views.carr_add, name='carr_add'),
    path('carrito/', views.carrito, name='carrito'),
    path('vac_carr/', views.vac_carr, name='vac_carr'),
    path('login/', views.login_view, name='login_views'),
    path('logout/', views.log_out, name='log_out'),
    path('registrarse/', views.register_view, name='register_views')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
