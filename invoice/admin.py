from django.contrib import admin
from .models import *


#// change the site name

admin.site.site_header = "INVOICE ADMIN"

# #//change the site title

# admin.site.site_title = "INVOICE ADMIN"


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','email', 'password',]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['product_name','product_discription']

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display=['Client_details','product_details','price','quantity','discount','sub_total']










