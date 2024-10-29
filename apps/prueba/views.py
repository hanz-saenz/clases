from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Blog, Categoria
from django.views import View

# Create your views here.
def bienvenida(request):
    return HttpResponse('Bienvenido a mi app')

def nueva_bienvenida(request):
    ## crear registro 1
    # crear_registro = Blog(titulo='Blog 2', contenido='Contenido del blog 2')
    # crear_registro.save()
    ## crear registro 2

    #crear_segundo_registro = Blog.objects.create(titulo='Blog 3', contenido='Contenido del blog 3')

    datos_blog = Blog.objects.all()
    return render(request, 'index.html', context={'datos_blog': datos_blog})


## Vistas basadas en clases

class MiVistaViews(View):

    def post(self, request):
        return HttpResponse('Esta es una vista POST')
    
    def get(self, request):
        print(request)
        return HttpResponse('Esta es una vista GET')
    

from django.views.generic import ListView, CreateView

class ListaBlog(ListView):
    model = Blog
    template_name = 'prueba/lista_productos.html'
    ordering = ['-id']

    def get_queryset(self):
        id_listar = 2
        # filtro_lista = self.model.objects.filter(id=id_listar)
        filtro_lista = self.model.objects.all()
        return filtro_lista

from django.urls import reverse_lazy

class CrearBlog(CreateView):
    model=Blog
    fields = ['titulo', 'contenido']
    template_name = 'prueba/crear_blog.html'
    success_url = reverse_lazy('lista_blogs')


from .forms import FormularioBlog
# Vista para el formulario
def nuevo_formulario(request):
    if request.method == 'POST':
        formulario = FormularioBlog(request.POST)
        if formulario.is_valid():
            subtitulo = formulario.cleaned_data['subtitulo']
            # archivo = request.FILES['archivo']
            print('subtitulo', subtitulo)
            print('archivo', request.FILES.get('archivo'))
            # formulario.save()
            return redirect('lista_blogs')
    else:
        formulario = FormularioBlog()
    return render(request, 'prueba/crear_blog.html', {'form': formulario})


# detalle blog 

def blog_detalle(request, id):
    # optimizada
    blog = get_object_or_404(Blog, pk=id)
    print('blog', blog.titulo)

    #opcíón por get
    blog_tres = Blog.objects.get(pk=id)
    print('blog_tres', blog_tres.titulo)
    # cuando se usa get o get_object_or_404 no necesitamos recorrer la variable
    # es decir solo ponemos la variable.campo 'blog_tres.titulo'

    # opción por filtro
    blog_dos = Blog.objects.filter(pk=id).order_by('-id')
    print('blog_dos', blog_dos)
    #para ver los datos del filter necesitamos recorrer la variable blog_dos

    for blog_d in blog_dos:
        print('blog_d', blog_d.titulo)


    return render(request, 'prueba/detalle.html', {'blog': blog_dos})
    

#eliminar blog
def eliminar_blog(request, id):
    blog = get_object_or_404(Blog, pk=id)
    if request.method == 'POST':
        blog.delete()
        return redirect('lista_blogs')
    
    return render(request, 'prueba/eliminar_blog.html', {'blog': blog})

#actualizar blog
def actualizar_blog(request, id):
    blog = get_object_or_404(Blog, pk=id)

    if request.method == 'POST':
        formulario = FormularioBlog(request.POST, instance=blog)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_blogs')
    else:
        formulario = FormularioBlog(instance=blog)

    return render(request, 'prueba/editar_blog.html', {'form': formulario})


#buscar blog
def buscar_blog(request):
    if request.GET.get('q'):
        query_buscar = request.GET.get('q')
    else:
        query_buscar = 'Espacio'
    resultados = Blog.objects.filter(titulo__icontains=query_buscar)
    return render(request, 'prueba/buscar.html', {'resultados': resultados})


# crear categoría
class CrearCategoria(CreateView):
    model=Categoria
    fields = ['nombre']
    template_name = 'prueba/crear_blog.html'
    success_url = reverse_lazy('lista_categorias')

# listarcategoria

class ListaCategoria(ListView):
    model = Categoria
    template_name = 'prueba/lista_categorias.html'
    ordering = ['-id']


from rest_framework.decorators import api_view
from rest_framework import generics, filters
from .serializers import BlogSerializer, CategoriaSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, BasePermission

class PaginaBlog(PageNumberPagination):
    page_size = 2



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
class NuevosPermisos(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.username == 'admin'
        else:
            return request.user.username == 'admin'
        return False

# Serializer personalizado para el token
class CustomTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username  # Agrega el nombre de usuario al token
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer


# Vista para manejar el blog
class VistaBlog(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # pagination_class = PaginaBlog
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo']
    permission_classes = [NuevosPermisos]




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class VistaDeBlogs(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def VistaDeBlogs2(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


class VistaUnBlog(APIView):
    def get(self, request, blog_id):
        blog = Blog.objects.filter(id=blog_id)
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

from django.views.decorators.csrf import csrf_exempt
@api_view(['POST'])
def crear_categoria(request):
    if request.method == 'POST':
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogListCrateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CategoriaListaCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def list(self, request, *args, **kwargs):
        print(self.get_queryset())
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    