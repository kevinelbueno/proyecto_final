from django.urls import path 
from . import views 
  
urlpatterns = [ 
    path("home/", views.home, name="home"), 
    path("ubicacion/", views.ubicacion, name="ubicacion"), 
    path("contactar/", views.contacto, name="contactar"), 
    path("tienda/", views.tienda, name="tienda"),
    path("menu/", views.menu, name="menu"),
    path("carro/", views.carro, name="carro"),
    path("redes/", views.redes, name="redes"),
    path("detalles/", views.detalles,name="detalles"),
    path("signup/", views.signup,name="signup"),
    path("signin/", views.signin,name="signin"),
    path('add_art/', views.add_art, name='add_art'),
    path('signout/', views.signout, name='signout'),
    path('art_detail/', views.art_list, name='art_list')
   
    
]