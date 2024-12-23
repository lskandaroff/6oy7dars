from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Flower, Type
from .forms import FlowerForm, TypeForm

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
        form =FlowerForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            flower = Flower.objects.create(**form.cleaned_data)
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
