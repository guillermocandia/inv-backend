# Generated by Django 2.0.1 on 2018-01-09 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='stock_min',
            field=models.IntegerField(blank=True, default=0, verbose_name='Stock Min'),
        ),
    ]
