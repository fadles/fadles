from django.shortcuts import render
from fadles.models import Product, House, PopularProduct


def home_view(request):
    products_list = Product.objects.all()
    popular_products_list = PopularProduct.objects.filter(is_active=True)
    return render(request, "main/main.html", locals())

def catalog_view(request):
    products_list = Product.objects.all()
    popular_products_list = PopularProduct.objects.filter(is_active=True)
    return render(request, "main/catalog.html", locals())

def product_view(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, "main/product.html", locals())

def catalog_houses_view(request):
    houses = House.objects.all()
    return render(request, "main/houses.html", locals())

def house_view(request, house_id):
    house = House.objects.get(pk=house_id)
    return render(request, "main/house.html", locals())

def review_view(request):
    return  render(request, "main/review.html")