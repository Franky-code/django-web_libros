from django.shortcuts import render
from django.views.generic import (TemplateView, ListView)


class IndexView(TemplateView):
    template_name = "home/index.html"
    
class ListaLibros(ListView):
    template_name = "home/lista.html"
    queryset = ['el quijote', 'python', 'flask']
    context_object_name = 'libros'