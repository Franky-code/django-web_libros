from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView,)
from .models import Autor, Libros


class IndexView(TemplateView):
    template_name = "home/index.html"
    
class ListaLibros(ListView):
    template_name = "home/lista.html"
    queryset = ['el quijote', 'python', 'flask']
    context_object_name = 'libros'


class ListaAutores(ListView):
    template_name = "biblioteca/lista-autores.html"
    model = Autor
    context_object_name = 'autores' 

class ListaLibrosAutores(ListView):
    template_name = "biblioteca/lista-libros.html"
    #model = Libros
    context_object_name = 'libros' 

    def get_queryset(self):
        id=self.kwargs["pk"]
        lista = Libros.objects.filter(autor=id)
        return lista

class AddAutor(CreateView):
    template_name='biblioteca/add-autor.html'
    model= Autor
    fields = ['nombre', 'nacionalidad']
    success_url = '/'