from django.contrib import admin
from .models import Product, DailySale, ProductLog

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'infinite_stock')
    search_fields = ('name',)

class DailySaleAdmin(admin.ModelAdmin):
    list_display = ('product', 'amount_sold', 'date')
    list_filter = ('date',)
    search_fields = ('product__name',)

# Update ProductLogAdmin based on the actual fields in your ProductLog model
class ProductLogAdmin(admin.ModelAdmin):
    list_display = ('product', 'amount_changed', 'date')  # Ensure 'amount_changed' is the correct field name
    list_filter = ('date',)
    search_fields = ('product__name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(DailySale, DailySaleAdmin)
admin.site.register(ProductLog, ProductLogAdmin)
