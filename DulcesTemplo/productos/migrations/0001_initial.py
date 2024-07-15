# Generated by Django 5.0.7 on 2024-07-14 16:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('descripcion', models.TextField()),
                ('categoria', models.CharField(max_length=255)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('moneda', models.CharField(default='PES', max_length=3)),
                ('cantidad_en_stock', models.PositiveIntegerField()),
                ('sku', models.CharField(max_length=100, unique=True)),
                ('upc', models.CharField(blank=True, max_length=12, null=True, unique=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('dimensiones', models.CharField(max_length=255)),
                ('imagenes', models.ImageField(blank=True, null=True, upload_to='productos/')),
                ('estado_producto', models.CharField(choices=[('nuevo', 'Nuevo'), ('usado', 'Usado'), ('reacondicionado', 'Reacondicionado')], max_length=50)),
                ('proveedor', models.CharField(max_length=255)),
                ('etiquetas', models.CharField(blank=True, max_length=255, null=True)),
                ('caracteristicas', models.JSONField(default=dict)),
                ('disponibilidad', models.CharField(choices=[('en_stock', 'En stock'), ('agotado', 'Agotado'), ('bajo_pedido', 'Bajo pedido')], max_length=50)),
                ('opiniones_valoraciones', models.JSONField(blank=True, default=list, null=True)),
                ('descuentos', models.JSONField(blank=True, default=dict, null=True)),
                ('envio', models.JSONField(default=dict)),
                ('garantia', models.TextField(blank=True, null=True)),
                ('instrucciones_uso', models.TextField(blank=True, null=True)),
                ('compatibilidad', models.TextField(blank=True, null=True)),
                ('fecha_vencimiento', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['nombre'],
            },
        ),
    ]
