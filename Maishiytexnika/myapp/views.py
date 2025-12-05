from django.shortcuts import render
from .models import Category, Texnika

def categories_page(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def texnika_list(request, pk):
    category = Category.objects.filter(pk=pk).first()
    texnikalar = Texnika.objects.filter(category=category) if category else []
    return render(request, 'texnika_list.html', {'category': category, 'texnikalar': texnikalar})

def texnika_detail(request, pk):
    texnika = Texnika.objects.filter(pk=pk).first()
    return render(request, 'texnika_detail.html', {'texnika': texnika})
