from django.contrib import admin
from .models import Products,Order
# Register your models here.

"""
admin.site.site_header = ""
admin.site.site_title = ""
admin.site.index_title = ""
"""

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_title','product_price')
    search_fields = ('product_title',)

    def change_category_to_default(self,request,queryset):
        queryset.update(product_categpry="default")
    change_category_to_default.short_description = 'Default Category'
    actions = ('change_category_to_default',)

    fields = ('product_title','product_price')

    list_editable = ('product_price',)

admin.site.register(Products,ProductsAdmin)
admin.site.register(Order)