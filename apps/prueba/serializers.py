from rest_framework import serializers
from .models import Blog, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']

class BlogSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()

    class Meta:
        model = Blog
        fields = ['id', 'titulo', 'contenido', 'categoria']

    def update(self, instance, validated_data):
        # Extrae la categoría
        categoria_data = validated_data.pop('categoria', None)
        
        # Actualiza los campos de Blog
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.contenido = validated_data.get('contenido', instance.contenido)

        # Si se proporcionó una categoría, actualízala
        if categoria_data:
            categoria_id = categoria_data.get('id', None)
            if categoria_id:
                instance.categoria = Categoria.objects.get(id=categoria_id)

        # Guarda los cambios en la instancia
        instance.save()
        return instance