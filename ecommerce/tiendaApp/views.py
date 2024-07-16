from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Producto, Cliente, TipoUsuario, Categoria, Editorial, Marca
from .forms import MangaForm, ClienteForm, EditorialForm, CategoriaForm, MarcaForm, TipoForm
from . import urls

def lista_productos(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'tiendaApp/lista_productos.html', context)

def ingresar_producto(request):
    if request.method == 'POST':
        form = MangaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = MangaForm()
    return render(request, 'tiendaApp/ingresar_producto.html', {'form': form})


def guardar_editorial(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = EditorialForm()
    return render(request, 'tiendaApp/guardar_editorial.html', {'form': form})

def guardar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = CategoriaForm()
    return render(request, 'tiendaApp/guardar_categoria.html', {'form': form})

def guardar_marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = MarcaForm()
    return render(request, 'tiendaApp/guardar_marca.html', {'form': form})

def guardar_tipo(request):
    if request.method == 'POST':
        form = TipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = TipoForm()

    context = {
        'form': form
    }
    return render(request, 'tiendaApp/guardar_tipo.html', {'form': form})








def index(request):
    return render(request, 'tiendaApp/index.html')

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'tiendaApp/listar_clientes.html', {'clientes': clientes})

def detalle_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    return render(request, 'tiendaApp/detalle_cliente.html', {'cliente': cliente})

def registrar_cliente(request):
    tipos_usuarios = TipoUsuario.objects.all()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()

    context = {
        'form': form,
    }
    return render(request, 'tiendaApp/registrar_cliente.html',context)


