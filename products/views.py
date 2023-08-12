from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm


# Vista Index
def index(request):

    productos = Producto.objects.all()[:9]

    context = {'productos': productos}

    return render(request, 'products/index.html', context)



#Vista Login
def login_view(request):
    if request.method == 'POST':

        # Procesar los datos del formulario de inicio de sesión
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Si las credenciales son válidas, iniciar sesión
            login(request, user)
            return redirect('dashboard')  # Redirigir a una página después del inicio de sesión exitoso
        else:
            # Si las credenciales no son válidas, mostrar un mensaje de error o volver a cargar la página de inicio de sesión
            context = {'error_message': 'Credenciales inválidas'}
            return render(request, 'products/login.html', context)

    return render(request, 'products/login.html')



#Vista Registro
def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('index')
        
        else:
            messages.error(request, 'Ocurrio un error durante el registro. Vuelve a intentarlo')
    
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'products/register.html', context)



#Cerrar Sesion
@login_required(login_url=('login'))

def cerrarSesion(request):
    logout(request)
    del request.session
    return redirect('index')


#Dashboard
@login_required(login_url=('login'))

def dashboard(request):

    productos = Producto.objects.all()[:6]

    usuario = request.user.first_name

    context = {'usuario': usuario, 'productos': productos}

    return render(request, 'products/dashboard.html', context)



#Agregar Productos
@login_required(login_url=('login'))

def agregarProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirige a la página del dashboard después de agregar el producto
    else:
        form = ProductoForm()

    context = {'form': form}
    return render(request, 'products/agregar.html', context)



#Visualizar Productos
@login_required(login_url=('login'))

def visualizarProducto(request):
    
    productos = Producto.objects.all()[:20]

    context = {'productos' : productos}
    return render(request, 'products/visualizar.html', context)


#Actualizar Productos
@login_required(login_url=('login'))

def actualizarProducto(request, pk):
    
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('visualizar')
        
    else:
        form = ProductoForm(instance=producto)

    context = {'form': form}

    return render(request, 'products/actualizar.html', context)



#Eliminar Productos
@login_required(login_url=('login'))

def eliminarProducto(request, pk):
    
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('visualizar')
    
    context = {'producto': producto}

    return render(request, 'products/eliminar.html', context)


#Perfil Productos
@login_required(login_url=('login'))

def perfilProducto(request, pk):
    
    producto = get_object_or_404(Producto, pk=pk)
    
    context = {'producto': producto}

    return render(request, 'products/perfil.html', context)



#Buscar Productos
@login_required(login_url=('login'))

def buscarProducto(request):
    
    if request.method == 'GET':
        query = request.GET.get('q', '')  # Obtenemos el término de búsqueda del parámetro 'q'
        resultados = Producto.objects.filter(nombre__icontains=query)  # Buscamos los productos por nombre
        
    else:
        resultados = None

    return render(request, 'products/buscar.html', {'resultados': resultados})