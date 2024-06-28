from django.urls import path 
from . import views 
  
urlpatterns = [
    path("home", views.home, name="home"), 
    path("ubicacion/", views.ubicacion, name="ubicacion"), 
    path("contactar/", views.contacto, name="contactar"), 
    path("tienda/", views.tienda, name="tienda"),
    path("menu/", views.menu, name="menu"),
    path("carro/", views.carro, name="carro"),
    path("redes/", views.redes, name="redes"),
    path("detalles/", views.detalles,name="detalle"),
    path("agregar/", views.agregar,name="agregar"),
    path("inicio_sesion/", views.agregar,name="agregar")
]