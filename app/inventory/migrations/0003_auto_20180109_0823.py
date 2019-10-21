# Generated by Django 2.0.1 on 2018-01-09 08:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_item_stock_min'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Name')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='comment',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='item',
            name='packaging',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Packgaing'),
        ),
        migrations.AddField(
            model_name='item',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.Brand'),
        ),
    ]