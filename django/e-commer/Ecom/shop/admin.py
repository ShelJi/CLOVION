from django.contrib import admin

from shop.models import UserData, ProductData, buyerData

admin.site.register(UserData)
admin.site.register(ProductData)
admin.site.register(buyerData)