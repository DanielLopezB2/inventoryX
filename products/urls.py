from django.urls import path
from . import views

urlpatterns = [
    
    #Index
    path('', views.index, name='index'), 

    #Login
    path('login/', views.login_view, name='login'), 
    #Registro
    path('registro/', views.registro, name ='registro'),
    #Logout
    path('logout/', views.cerrarSesion , name='logout'),

    #Dashboard
    path('dashboard/', views.dashboard , name='dashboard'),

    #Agregar producto
    path('agregar/', views.agregarProducto , name='agregar'),
    #Visualizar producto
    path('visualizar/', views.visualizarProducto , name='visualizar'),
    #Actualizar producto
    path('actualizar/<int:pk>', views.actualizarProducto , name='actualizar'),
    #Eliminar producto
    path('eliminar/<int:pk>', views.eliminarProducto , name='eliminar'),

    #Perfil producto
    path('perfil/<int:pk>', views.perfilProducto , name='perfil'),

    #Buscar producto
    path('buscar/', views.buscarProducto , name='buscar'),

    ]