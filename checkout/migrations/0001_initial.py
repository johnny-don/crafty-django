# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-28 16:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_auto_20200320_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default=b'', max_length=50)),
                ('phone_number', models.CharField(default=b'', max_length=20)),
                ('country', models.CharField(default=b'', max_length=40)),
                ('postcode', models.CharField(blank=True, max_length=20)),
                ('town_or_city', models.CharField(default=b'', max_length=40)),
                ('street_address1', models.CharField(default=b'', max_length=40)),
                ('street_address2', models.CharField(default=b'', max_length=40)),
                ('county', models.CharField(default=b'', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
