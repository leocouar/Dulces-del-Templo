from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        # fields = [
        #     'id', 'nombre', 'descripcion', 'categoria', 'precio', 'moneda',
        #     'cantidad_en_stock', 'sku', 'upc', 'fecha_creacion', 'fecha_actualizacion',
        #     'peso', 'dimensiones', 'imagenes', 'estado_producto', 'proveedor',
        #     'etiquetas', 'caracteristicas', 'disponibilidad', 'opiniones_valoraciones',
        #     'descuentos', 'envio', 'garantia', 'instrucciones_uso', 'compatibilidad',
        #     'fecha_vencimiento'
        # ]
        fields = '__all__'
    imagenes = serializers.ImageField(max_length=None,allow_empty_file=True, use_url=True)