from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Sale
from .models import SaleItem
from .models import PaymentMethod
from .serializers import SaleSerializer
from .serializers import SaleItemSerializer
from .serializers import SaleActiveSerializer
from .serializers import PaymentMethodSerializer
from .filters import SaleFilter


class SaleList(generics.ListCreateAPIView):
    """
    get:
        Lista de ventas.
    post:
        Crea venta.
    """

    queryset = Sale.objects.all().order_by('-date')
    serializer_class = SaleSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = SaleFilter


class SaleDetail(generics.RetrieveAPIView):
    """
    get:
        Retorna venta.
    """

    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class SaleActiveDetail(generics.UpdateAPIView):
    """
    put:
        Anula venta.
    """

    queryset = Sale.objects.all()
    serializer_class = SaleActiveSerializer


class PaymentMethodList(generics.ListCreateAPIView):
    """
    get:
        Lista medios de pago.
    post:
        Crea medio de pago.
    """

    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer


class PaymentMethodDetail(generics.RetrieveUpdateAPIView):
    """
    get:
        Retorna medio de pago.
    put:
        Actuliza medio de pago.
    """

    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
