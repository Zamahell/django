from django.urls import path
from . import views

urlpatterns = [
    path('',                            views.index,             name='index'),
    path('productos/',                  views.lista_productos,   name='lista_productos'),
    path('productos/ingresar/',         views.ingresar_producto, name='ingresar_producto'),
    path('editorial/',                  views.guardar_editorial, name='guardar_editorial'),
    path('categoria/',                  views.guardar_categoria, name='guardar_categoria'),
    path('marca/',                      views.guardar_marca,     name='guardar_marca'),
    path('tipo/',                       views.guardar_tipo,      name='guardar_tipo'),
    path('clientes/',                   views.listar_clientes,   name='listar_clientes'),
    path('clientes/<int:cliente_id>/',  views.detalle_cliente,   name='detalle_cliente'),
    path('clientes/registrar/',         views.registrar_cliente, name='registrar_cliente'),
]
