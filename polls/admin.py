from django.contrib import admin

from polls.models import Opcao, Pergunta

# Register your models here.
admin.site.register(Pergunta)
admin.site.register(Opcao)
