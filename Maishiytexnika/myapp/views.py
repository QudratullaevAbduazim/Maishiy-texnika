from django.shortcuts import render, redirect
from .models import Category, Texnika
from django.contrib import messages
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





def create_texnika(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        year = request.POST.get('year')
        image = request.FILES.get('image')
        brand_id = request.POST.get('brand')
        category_id = request.POST.get('category')

        texnika = Texnika(
            name=name,
            desc=desc,
            price=price,
            year=year,
            image=image,
            brand_id=brand_id,
            category_id=category_id,
        )
        texnika.save()

        messages.success(request, 'Texnika muvaffaqiyatli yaratildi')
        return redirect('texnika_detail', pk=texnika.pk)

    return render(request, 'create_texnika.html')



def update_texnika(request, pk):
    texnika = Texnika.objects.get(pk=pk)

    if request.method == "POST":
        texnika.name = request.POST.get("name")
        texnika.desc = request.POST.get("desc")
        texnika.price = request.POST.get("price")
        texnika.year = request.POST.get("year")
        if request.FILES.get("image"):
            texnika.image = request.FILES.get("image")
        texnika.brand_id = request.POST.get("brand")
        texnika.category_id = request.POST.get("category")
        texnika.save()

        # Xabar qo'shish
        messages.success(request, "Texnika muvaffaqiyatli o'zgartirildi!")

        # Yangilangan sahifaga yo'naltirish
        return redirect("update_texnika", pk=texnika.pk)

    return render(request, "update_texnika.html", {"texnika": texnika})


def delete_texnika(request, pk):
    texnika = Texnika.objects.get(pk=pk)
    if request.method == "POST":
        texnika.delete()
        messages.info(request, 'Mashina ochirildi')
        return redirect('categories_page')
    return render(request, "delete_texnika.html", {"texnika": texnika})





















