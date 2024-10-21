from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Blog(models.Model):
    titulo = models.CharField(max_length=300, null=False, blank=False)
    contenido = models.TextField(null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, verbose_name='Mi categoría')

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.titulo} - {str(self.id)}'