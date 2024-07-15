from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    moneda = models.CharField(max_length=3, default='PES')
    cantidad_en_stock = models.PositiveIntegerField()
    sku = models.CharField(max_length=100, unique=True)
    upc = models.CharField(max_length=12, unique=True, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    dimensiones = models.CharField(max_length=255)
    imagenes = models.ImageField(upload_to='productos/images/', blank=True, null=True)
    estado_producto = models.CharField(max_length=50, choices=[
        ('nuevo', 'Nuevo'),
        ('usado', 'Usado'),
        ('reacondicionado', 'Reacondicionado')
    ])
    proveedor = models.CharField(max_length=255)
    etiquetas = models.CharField(max_length=255, blank=True, null=True)
    caracteristicas = models.JSONField(default=dict)
    disponibilidad = models.CharField(max_length=50, choices=[
        ('en_stock', 'En stock'),
        ('agotado', 'Agotado'),
        ('bajo_pedido', 'Bajo pedido')
    ])
    opiniones_valoraciones = models.JSONField(default=list, blank=True, null=True)
    descuentos = models.JSONField(default=dict, blank=True, null=True)
    envio = models.JSONField(default=dict)
    garantia = models.TextField(blank=True, null=True)
    instrucciones_uso = models.TextField(blank=True, null=True)
    compatibilidad = models.TextField(blank=True, null=True)
    fecha_vencimiento = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = _("Producto")
        verbose_name_plural = _("Productos")
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
