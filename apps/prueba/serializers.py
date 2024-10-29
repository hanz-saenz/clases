from rest_framework import serializers
from .models import Blog, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']

class BlogSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    blogs_count = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = ['id','titulo', 'contenido', 'categoria', 'blogs_count']

    def get_blogs_count(self, obj):
        return 'obj.categoria.count()'
    
    def update(self, instance, validated_data):
        # Si categoria es un campo anidado
        categoria_data = validated_data.pop('categoria', None)
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.contenido = validated_data.get('contenido', instance.contenido)
        # Si estás manejando un campo anidado, necesitas gestionarlo aquí
        if categoria_data:
            instance.categoria = categoria_data
        instance.save()
        return instance