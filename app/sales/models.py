from django.db import models
import uuid

from app.inventory.models import Item


class PaymentMethod(models.Model):
    """
    Payment Method
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
       verbose_name='Name',
       max_length=64,
       blank=False,
       null=False,
       unique=True
    )

    active = models.BooleanField(
        verbose_name='Active',
        blank=True,
        null=False,
        default=True
    )

    class Meta:
        verbose_name = 'Payment method'
        verbose_name_plural = 'Payment methods'

    def __str__(self):
        return self.name


class Sale(models.Model):
    """
    Sale
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    date = models.DateTimeField(
        verbose_name='Date',
        blank=True,
        null=False,
        auto_now_add=True
    )

    total = models.IntegerField(
        verbose_name='Total',
        blank=True,
        null=False,
        default=0
    )

    paymentmethod = models.ForeignKey(
        PaymentMethod,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    active = models.BooleanField(
        verbose_name='Active',
        blank=True,
        null=False,
        default=True
    )

    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'

    def __str__(self):
        return '{}: {}'.format(self.date, self.total)

    def calculateTotal(self):
        total = 0
        for item in self.saleitem_set.all():
            total += item.price * item.quantity
        self.total = total
        self.save()

    def updateInventory(self, operation=-1):
        for saleitem in self.saleitem_set.all():
            item = saleitem.item
            item.stock += saleitem.quantity * operation
            item.save()


class SaleItem(models.Model):
    """
    Sale Item
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    item = models.ForeignKey(
        Item,
        null=True,
        blank=False,
        on_delete=models.DO_NOTHING
    )

    price = models.IntegerField(
        verbose_name='Price',
        blank=False,
        null=False,
        default=0
    )

    quantity = models.IntegerField(
        verbose_name='Quantity',
        blank=False,
        null=False,
        default=0
    )

    sale = models.ForeignKey(
        Sale,
        null=True,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Sale Item'
        verbose_name_plural = 'Sale Items'

    def __str__(self):
        return '{}: {}'.format(self.item.name, self.quantity)
