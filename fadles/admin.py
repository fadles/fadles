from fadles.models import Product, ProductImage, ProductCertificate, HouseImage, House, Sale, PopularProduct, ProductTable
from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group, User
from django.contrib.flatpages.models import FlatPage

# Note: we are renaming the original Admin and Form as we import them!
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld

from django import forms
from ckeditor.widgets import CKEditorWidget

class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = FlatPage # this is not automatically inherited from FlatpageFormOld


class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm

class ProductTableInline(admin.TabularInline):
    model = ProductTable

class ProductImageInline(AdminImageMixin, admin.TabularInline):
    model = ProductImage

class ProductCertificateInline(AdminImageMixin, admin.TabularInline):
    model = ProductCertificate

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductCertificateInline, ProductTableInline]


class HouseImageInline(AdminImageMixin, admin.TabularInline):
    model = HouseImage

class HouseAdmin(admin.ModelAdmin):
    inlines = [HouseImageInline, ]

admin.site.register(Product, ProductAdmin)
admin.site.register(House, HouseAdmin)
admin.site.unregister(Group)
admin.site.unregister(Site)
# admin.site.unregister(User)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(PopularProduct)
admin.site.register(Sale)
