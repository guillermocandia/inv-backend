from django_filters.rest_framework import FilterSet

from .models import Sale


class SaleFilter(FilterSet):
    class Meta:
        model = Sale
        fields = {
            'date': ['lte', 'gte'],
            'active': ['exact'],
            'paymentmethod': ['exact']
        }
