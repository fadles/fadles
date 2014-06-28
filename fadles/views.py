from django.shortcuts import render
from fadles.models import Product


def home_view(request):
    products_list = Product.objects.all()
    return render(request, "main/main.html", locals())

def catalog_view(request):
    products_list = Product.objects.all()
    return render(request, "main/catalog.html", locals())

def product_view(request, product_id):
    return render(request, "main/product.html", locals())

def catalog_houses_view(request):
    return render(request, "main/houses.html", locals())

def house_view(request, house_id):
    return render(request, "main/house.html", locals())