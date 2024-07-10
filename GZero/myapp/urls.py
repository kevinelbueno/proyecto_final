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
    path("detalles2/", views.detalles2,name="detalle2"),
    path("signup/", views.signup,name="signup"),
    path("signin/", views.signin,name="signin"),
    path('add_art/', views.add_art, name='add_art'),
    path('signout/', views.signout, name='signout'),
    path('art_detail/', views.art_list, name='art_list'),
    path('art_list_AD/', views.art_list_AD, name='art_list_AD'),
    path('delete_art/<int:art_id>/', views.delete_art, name='delete_art')
   
    
]