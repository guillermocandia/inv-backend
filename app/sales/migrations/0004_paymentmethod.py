# Generated by Django 2.0.1 on 2018-01-30 20:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_sale_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Name')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'verbose_name': 'Payment method',
                'verbose_name_plural': 'Payment methods',
            },
        ),
    ]
