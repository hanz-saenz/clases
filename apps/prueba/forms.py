from django import forms
from .models import Blog


class FormularioBlog(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['titulo','contenido', 'categoria']