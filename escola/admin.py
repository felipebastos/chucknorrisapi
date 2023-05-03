from django.contrib import admin

from escola.models import Artigo, Autor, Livro, Submissao

# Register your models here.
admin.site.register(Autor)
admin.site.register(Livro)
admin.site.register(Artigo)
admin.site.register(Submissao)
