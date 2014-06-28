from fadles.models import Product, ProductImage, ProductCertificate, HouseImage, House
from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group, User


class ProductImageInline(AdminImageMixin, admin.TabularInline):
    model = ProductImage

class ProductCertificateInline(AdminImageMixin, admin.TabularInline):
    model = ProductCertificate

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductCertificateInline]


class HouseImageInline(AdminImageMixin, admin.TabularInline):
    model = HouseImage

class HouseAdmin(admin.ModelAdmin):
    inlines = [HouseImageInline, ]

admin.site.register(Product, ProductAdmin)
admin.site.register(House, HouseAdmin)
admin.site.unregister(Group)
admin.site.unregister(Site)
# admin.site.unregister(User)
