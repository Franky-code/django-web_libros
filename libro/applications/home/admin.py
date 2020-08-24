from django.contrib import admin
from .models import Autor, Libros

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad', 'id')
    
    search_fields = ('nombre', 'nacionalidad',)

class LibrosAdmin(admin.ModelAdmin):
    list_display = ('title', 'resume', 'autor', 'id',)
    
    search_fields = ('title',)

    list_filter = ('autor',)

admin.site.register(Autor, AutorAdmin)
admin.site.register(Libros, LibrosAdmin)

