# coding=utf-8
import json
from django.http import HttpResponseRedirect
from django.shortcuts import render
from fadles.models import Product, House, PopularProduct, ProductTable, ContactUs, Sale
from forms import ContactUsForm
from django.contrib import messages


def home_view(request):
    products_list = Product.objects.all()
    popular_products_list = PopularProduct.objects.filter(is_active=True)
    sales = Sale.objects.filter(is_active=True)
    return render(request, "main/main.html", locals())

def catalog_view(request):
    products_list = Product.objects.all()
    popular_products_list = PopularProduct.objects.filter(is_active=True)
    return render(request, "main/catalog.html", locals())

def product_view(request, product_id):
    product = Product.objects.get(pk=product_id)
    product_tables = product.tables.all()
    for table in product_tables:
        table.table_json = json.loads(table.table_json)
        table.table_json = [sorted(row.items()) for row in table.table_json ]
        print table.table_json

    return render(request, "main/product.html", locals())

def catalog_houses_view(request):
    houses = House.objects.all()
    return render(request, "main/houses.html", locals())

def house_view(request, house_id):
    house = House.objects.get(pk=house_id)
    return render(request, "main/house.html", locals())

def review_view(request):
    return  render(request, "main/review.html")

def contactus_view(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            ContactUs(**form.cleaned_data).save()
            messages.add_message(request,messages.SUCCESS,'Ваше сообщение успешно отправлено')
            return HttpResponseRedirect('/contacts/')
        messages.add_message(request,messages.ERROR,'Пожалуйста проверьте правильность ввода информации')
    else:
        form = ContactUsForm()
    return  render(request, "main/contact_us.html", locals())