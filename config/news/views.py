from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Flower, Type

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
