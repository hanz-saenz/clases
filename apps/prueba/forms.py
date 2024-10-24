from django import forms
from .models import Blog


class FormularioBlog(forms.ModelForm):


    ESTADOS = [
        ('Activo', 'Activo'),
        ('Activo', 'Inactivo'),
    ]
    subtitulo = forms.CharField(max_length=300, required=False, 
                                widget=forms.TextInput(
                                    attrs={'id': 'subtitulo_id', 'class': 'form-control'}))  
    
    daterange = forms.CharField(label='Rango de fechas', max_length=300, required=False,
                                widget=forms.TextInput(
                                    attrs={
                                        'id': 'daterange', 
                                        'name': 'daterange_name',
                                        'class': 'form-control',

                                        }))

    archivo = forms.FileField(label='Subir Archivo', required=False)

    destacado = forms.BooleanField(required=False)
    estado = forms.ChoiceField(choices=ESTADOS, required=False)

    class Meta:
        model = Blog
        fields = ['titulo','contenido', 'categoria', 'fecha_publicacion']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa el Título',
                'id': 'id_titulo',
            }),
            'contenido': forms.Textarea(attrs={
                'rows': 4,
                'cols': 50,
                'required': False,
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control',
            }),
            'fecha_publicacion': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True,
            })
        }

