from django import forms
from .models import Cliente, Producto, Categoria, Editorial, TipoUsuario, FormaPago, Editorial, Marca

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut', 'nombre', 'apellido', 'correo', 'tipo_usuario']

class MangaForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo_barra', 'descripcion', 'precio_costo', 'precio_venta', 'editorial', 'categoria', 'marca']

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ['nombre', 'estado']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'estado']

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre', 'estado']

class TipoForm(forms.ModelForm):
    class Meta:
        model = TipoUsuario
        fields = ['nombre', 'estado']