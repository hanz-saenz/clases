from django.urls import path
from .views import *

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('mivista/', MiVistaViews.as_view(), name='mi_vista'),
    path('blogs/', ListaBlog.as_view(), name='lista_blogs'),
    path('blogs/create', CrearBlog.as_view(), name='crear_blog'),
    path('blog/nuevo', nuevo_formulario, name='nuevo_blog'),
    path('blog/detalle/<int:id>', blog_detalle, name='detalle_blog'),
    path('blog/eliminar/<int:id>', eliminar_blog, name='eliminar_blog'),
    path('blog/editar/<int:id>', actualizar_blog, name='actualizar_blog'),
    path('blog/buscar/', buscar_blog, name='buscar_blog'),

    path('blogs/categorias', ListaCategoria.as_view(), name='lista_categorias'),
    path('blogs/create/categoria', CrearCategoria.as_view(), name='crear_categoria'),

    path('api/blogs', VistaBlog.as_view(), name='api_blogs'),
    path('api/blogs2', VistaDeBlogs.as_view(), name='api_blogs2'),
    path('api/blogf/', VistaDeBlogs2, name='api_blogf'),

    path('api/blog/<int:blog_id>', VistaUnBlog.as_view(), name='aapi_detalles_blog'),
    path('api/blog/crear/', crear_categoria, name='blo_crear_api'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/lista_blogs/', BlogListCrateView.as_view(), name='api_lista_blogs'),
    path('api/lista_blogs/<int:pk>', BlogDetailView.as_view(), name='api_lista_blogs_details'),
    path('api/lista_categorias/', CategoriaListaCreateView.as_view(), name='api_lista_categorias'),
    path('api/blogselect/', vista_select_related, name='blogselect'),
    path('sentry-debug/', trigger_error),

]