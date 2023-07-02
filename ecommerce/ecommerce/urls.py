"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from store.views import home_view, login_view, logout_view, register_view, MiCuentaView, EliminarDireccionView, EditarDireccionView, AgregarDireccionView, producto_detalle_view

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('mi-cuenta/', MiCuentaView.as_view(), name='mi_cuenta'),
    path('editar-direccion/<int:pk>/', EditarDireccionView.as_view(), name='editar_direccion'),
    path('eliminar-direccion/<int:pk>/', EliminarDireccionView.as_view(), name='eliminar_direccion'),
    path('agregar-direccion/', AgregarDireccionView.as_view(), name='agregar_direccion'),
    path('producto/<int:id>/', producto_detalle_view, name='producto_detalle'),
]
