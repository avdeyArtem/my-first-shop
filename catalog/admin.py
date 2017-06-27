from django.contrib import admin
from catalog.models import CategoriesFirst,CategoriesSecond, Product, Brand, Order
admin.site.register(Product)
admin.site.register(CategoriesFirst)
admin.site.register(CategoriesSecond)
admin.site.register(Brand)
admin.site.register(Order)
