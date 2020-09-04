from django.shortcuts import render, redirect
from .models import Producto, Category
from django.contrib.auth import login, logout,authenticate
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from app_tienda.forms import LoginForms, RegisterForm, Departamentos_filter
from django.shortcuts import HttpResponse

# Create your views here.


def index(req):

    productos = Producto
    q = req.GET.get('q', None)
    if q is None or q == '':
        productos = Producto.objects.all()
    elif q is not None:
        productos = Producto.objects.filter(title__contains=q)


    return render(req, 'app_tienda/index.html', {'productos': productos})


def login_view(req):
    mensaje = ""
    if req.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if req.method == 'POST':
            form = LoginForms(req.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username, password=password)
                if usuario is not None and usuario.is_active:
                    login(req, usuario)
                    return HttpResponseRedirect('/')
                else:
                    mensaje = "Usuario y/o contraseña incorrecta"
        form = LoginForms
        return render(req, 'app_tienda/login.html', {'form': form, 'mensaje': mensaje})


def log_out(req):
    logout(req)
    return HttpResponseRedirect('/')


def register_view(req):
    form = RegisterForm
    if req.method == "POST":
        form = RegisterForm(req.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password_1 = form.cleaned_data['password_1']
            password_2 = form.cleaned_data['password_2']
            u = User.objects.create_user(username=usuario, email=email, password=password_1)
            u.save()
            return render(req, 'app_tienda/registrado.html')
        else:
            form = form

    return render(req, 'app_tienda/registrarse.html', {'form': form})


def alimentos_ref(req):

    productos = Producto.objects.filter(category__title='Alimentos Refrigerados')

    return render(req, 'app_tienda/index.html', {'productos': productos})


def alimentos(req):

    productos = Producto.objects.filter(category__title='Alimentos')

    return render(req, 'app_tienda/index.html', {'productos': productos})


def util_hog(req):

    productos = Producto.objects.filter(category__title='Utiles del Hogar')

    return render(req, 'app_tienda/index.html', {'productos': productos})

comprado_x_user = {}


@login_required(login_url='login_views')
def carr_add(req, id):
    username = req.user
    producto = Producto.objects.get(id=id)
    if username not in comprado_x_user.keys():
        list = [producto]
        comprado_x_user.update({username: list })
    else:
        val = comprado_x_user.get(username)
        val.append(producto)


    return redirect('index')


def vac_carr(req):
    username = req.user
    lista = comprado_x_user.get(username)
    lista.clear()

    return redirect('index')

@login_required(login_url='login_views')
def carrito(req):
    username = req.user
    productos = comprado_x_user.get(username)
    cant = int
    total = 0
    if productos:
        cant = len(productos)
        for pro in productos:
                total = total + pro.precio


    return render(req, 'app_tienda/carrito.html', {'productos': productos, 'cant': cant, 'total': round(total, 2)})




