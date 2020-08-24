from django.urls import path, re_path, include

from . import views

app_name="home_app"


urlpatterns = [
    path('index', views.IndexView.as_view(), name='index'),
    path('libros', views.ListaLibros.as_view(), name='lista'),
    path('', views.ListaAutores.as_view(), name='lista-autores'),
    path('libros-autor/<pk>/por-autor', views.ListaLibrosAutores.as_view(), name='lista-libros'),
]
