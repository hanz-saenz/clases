from django.urls import path
from .views import crear_categoria, VistaUnBlog, VistaDeBlogs2,MiVistaViews, ListaBlog, CrearBlog, nuevo_formulario, blog_detalle, eliminar_blog, actualizar_blog , buscar_blog, ListaCategoria, CrearCategoria, VistaBlog, VistaDeBlogs

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
]