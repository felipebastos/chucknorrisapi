from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext

from escola.models import Artigo, Autor, Livro, Submissao


# Register your models here.
class AutorAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "categoria", "artigos_enviados"]
    ordering = ("id", "nome", "categoria")

    search_fields = ["nome"]

    list_filter = ["categoria"]

    actions = ["tornar_discente"]

    @admin.display(description="Artigos")
    def artigos_enviados(self, obj):
        return f"{len(obj.artigos.all())}"

    @admin.action(description="Tornar discente")
    def tornar_discente(self, request, queryset):
        updated = queryset.update(categoria="DIS")
        self.message_user(
            request,
            ngettext(
                "%d autor atualizado como discente",
                "%d autores atualizados como discentes",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )


admin.site.register(Autor, AutorAdmin)
admin.site.register(Livro)
admin.site.register(Artigo)
admin.site.register(Submissao)

admin.site.site_title = "Chuck Norris API"
admin.site.index_title = "Página inicial do CN-API"
admin.site.site_header = "Chuck Norris Admin"
