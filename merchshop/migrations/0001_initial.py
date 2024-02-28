# Generated by Django 5.0.2 on 2024-02-28 03:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_id', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=31)),
                ('descn', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('product_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='merchshop.producttype')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
