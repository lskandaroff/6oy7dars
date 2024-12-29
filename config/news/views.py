from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect

from .models import Flower, Type
from .forms import FlowerForm, TypeForm, RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

def home(request):
    flowers = Flower.objects.all()

    context = {
        "flowers": flowers,
        'title': "Barcha maqolalar"
    }

    return render(request, 'index.html', context)

def flower_by_type(request, type_id):
    flowers = get_list_or_404(Flower, type_id=type_id)
    types = get_object_or_404(Type, pk=type_id)


    context = {
        'flowers':flowers,
        'title': f"{types.name}: barcha maqolalar"
    }
    return render(request, 'index.html', context)

def about_flowers(request, flower_id):
    flowers = get_object_or_404(Flower, id=flower_id)

    flowers.views += 1
    flowers.save()

    context = {
        'flowers': flowers,
        'title': flowers.name
    }



    return render(request, 'details.html', context)

def add_flower(request: WSGIRequest):

    if request.method == "POST":
        form = FlowerForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            flower = form.create()
            print(flower, 'qoshildi!')

    forms = FlowerForm()

    context = {
        'forms': forms
    }

    return render(request, 'add_flower.html', context)

def add_type(request: WSGIRequest):

    if request.method == "POST":
        form =TypeForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            type = Type.objects.create(**form.cleaned_data)
            print(type, 'qoshildi!')

    forms = TypeForm()

    context = {
        'forms': forms
    }

    return render(request, 'add_type.html', context)

def update_flower(request: WSGIRequest, flower_id):
    flower = get_object_or_404(Flower, pk=flower_id)

    if request.method == "POST":
        form = FlowerForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.update(flower)
            messages.success(request, 'Maqola ozgartirildi')



    forms = FlowerForm(initial={
        'name': flower.name,
        'color': flower.color,
        'description': flower.description,
        'price': flower.price,
        'photo': flower.photo,

    })

    context = {
        'forms': forms,
    }

    return render(request, 'add_flower.html', context)

def delete_flower(request, flower_id):
    flower = get_object_or_404(Flower, pk=flower_id)
    if request.method == 'POST':
        flower.delete()
        messages.success(request, 'Maqola ochirildi')
        return redirect('home')

    context = {
        'flower': flower
    }
    return render(request, 'confirm_delete.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            password_repeat = form.cleaned_data.get('password_repeat')
            if password == password_repeat:
                user = User.objects.create_user(
                    form.cleaned_data.get('username'),
                    form.cleaned_data.get('email'),
                    password
                )
                messages.success(request, 'Registeratsiya muvaffaqiyatli boldi')
                return redirect('login')

    context = {
        'form': RegisterForm()
    }
    return render(request, 'auth/register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            messages.success(request, 'Xush kelibsiz')
            login(request, user)
            return redirect('home')
    context = {
        'form': LoginForm()
    }

    return render(request, 'auth/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')












