from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category
from .models import Brand
from .models import Item
from .serializers import CategorySerializer
from .serializers import BrandSerializer
from .serializers import ItemSerializer
from .filters import CategoryFilter
from .filters import BrandFilter
from .filters import ItemFilter


class CategoryList(generics.ListCreateAPIView):
    """
    get:
        Retorna lista de Categorias.
    post:
        Crea Category.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_class = CategoryFilter
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name', 'active')


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
        Retorna Categoria.
    put:
        Modifica Categoria.
    delete:
        Borra Categoria.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandList(generics.ListCreateAPIView):
    """
    get:
        Retorna lista de Marcas.
    post:
        Crea Marca.
    """

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_class = BrandFilter
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name', 'active')


class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
        Retorna Marca.
    put:
        Modifica Marca.
    delete:
        Borra Marca.
    """

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ItemList(generics.ListCreateAPIView):
    """
    get:
        Retorna lista de Items.
    post:
        Crea Item.
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_class = ItemFilter
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('name', 'bar_code')
    ordering_fields = ('name', 'bar_code', 'stock',
                       'stock_min', 'price', 'active')


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
        Retorna Item.
    put:
        Modifica Item.
    delete:
        Borra Item.
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
