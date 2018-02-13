from django_filters.rest_framework import FilterSet

from .models import Category
from .models import Brand
from .models import Item


class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields = ['active']


class BrandFilter(FilterSet):
    class Meta:
        model = Brand
        fields = ['active']


class ItemFilter(FilterSet):
    class Meta:
        model = Item
        fields = ['category', 'brand', 'active']
