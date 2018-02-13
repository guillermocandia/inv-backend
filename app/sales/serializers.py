from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from .models import Sale
from .models import SaleItem
from .models import PaymentMethod
from app.inventory.models import Item
# from app.inventory.serializers import ItemSerializer


class PaymentMethodSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethod
        fields = '__all__'


class PaymentMethodSerializer2(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethod
        fields = '__all__'
        extra_kwargs = {
            'name': {'validators': []}
        }


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        extra_kwargs = {
            'name': {'validators': []},
            'bar_code': {'validators': []}
        }


class SaleItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = SaleItem
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    saleitem_set = SaleItemSerializer(many=True)
    paymentmethod = PaymentMethodSerializer2()

    class Meta:
        model = Sale
        fields = '__all__'

    def create(self, validated_data):
        from pprint import pprint
        saleitems_data = validated_data.pop('saleitem_set')
        paymentmethod_data = validated_data.pop('paymentmethod')
        paymentmethod = PaymentMethod.objects.\
            get(name=paymentmethod_data.get('name'))
        sale = Sale.objects.create(**validated_data)
        sale.paymentmethod = paymentmethod
        for saleitem in saleitems_data:
            aux_item = saleitem['item']
            item = Item.objects.get(bar_code=aux_item.get('bar_code'))
            saleitem['item'] = item
            SaleItem.objects.create(sale=sale, **saleitem)
        sale.calculateTotal()
        sale.updateInventory()
        return sale

# Se crea un nuevo serializador pata Items para evitar la validación
# de campos únicos.

# Se define create en SaleSerializer
# se crea una instancia de item a partir del código de barras, ya no viene
# el id item en validated_data
# (los serializadores no reciben el id porque viene en la URL)

# Una solución alternativa podria ser forzar en el serilizador recibir un id,
# pero generaria problemas(habría que definir cuando usar ese id)

# Con la solución actual se evita tener que sobreescribir métodos en las vistas

# https://medium.com/django-rest-framework/dealing-with-unique-constraints-in-nested-serializers-dade33b831d9
# https://stackoverflow.com/questions/38438167/unique-validation-on-nested-serializer-on-django-rest-framework

# Se aplica lo mismo de arriba con los medios de Pago
# Se crearon 2 serializadores, solo uno válida


class SaleActiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = ['active']

    def update(self, instance, validated_data):
        active = validated_data.get('active')

        if(active):
            raise PermissionDenied()

        if(not instance.active):
            raise PermissionDenied()

        instance.updateInventory(operation=1)
        instance.active = active
        instance.save()
        return instance
