from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin): # To show the slug as display items on admin
    list_display = ['__str__', 'slug']
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
