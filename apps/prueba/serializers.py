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
        fields = ['titulo', 'contenido', 'categoria', 'blogs_count']

    def get_blogs_count(self, obj):
        return 'obj.categoria.count()'
    
