from django.shortcuts import render
from fadles.models import Product


def home(request):
    products_list = Product.objects.all()
    return render(request, "main/main.html", locals())