from django.contrib import admin
from .models import ShopCart


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'quantity', 'price', 'amount']
    list_filter = ['user', 'product']
    list_per_page = 10
    search_fields = ['product', 'user']


# Register your models here.
admin.site.register(ShopCart, ShopCartAdmin)
