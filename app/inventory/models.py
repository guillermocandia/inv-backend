from django.db import models
import uuid


class Category(models.Model):
    """
    Category
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
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Brand(models.Model):
    """
    Brand
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
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name


class Item(models.Model):
    """
    Item
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

    price = models.IntegerField(
        verbose_name='Price',
        blank=True,
        null=False,
        default=0
    )

    bar_code = models.CharField(
        verbose_name='Bar Code',
        max_length=64,
        blank=True,
        null=True,
        unique=True
    )

    packaging = models.CharField(
        verbose_name='Packgaing',
        max_length=128,
        blank=True,
        null=True
    )

    stock = models.IntegerField(
        verbose_name='Stock',
        blank=True,
        null=False,
        default=0
    )

    comment = models.CharField(
        verbose_name='Comment',
        max_length=256,
        blank=True,
        null=True
    )

    stock_min = models.IntegerField(
        verbose_name='Stock Min',
        blank=True,
        null=False,
        default=0
    )

    category = models.ManyToManyField(
        Category,
        blank=True
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    active = models.BooleanField(
        verbose_name='Active',
        blank=True,
        null=False,
        default=True
    )

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name
