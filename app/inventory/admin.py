from django.contrib import admin

from .models import Category
from .models import Brand
from .models import Item


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active']
    list_editable = ['active']


class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active']
    list_editable = ['active']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active']
    list_editable = ['active']
    list_filter = ['category', 'brand']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Item, ItemAdmin)
