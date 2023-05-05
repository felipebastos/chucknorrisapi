""" Painel administrativo de Escola """
from datetime import date

from django.contrib import admin, messages
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext

from escola.models import Artigo, Autor, Livro, Submissao


# Register your models here.
class AutorAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "categoria", "artigos_enviados", "livros_publicados"]
    ordering = ("id", "nome", "categoria")

    search_fields = ["nome"]

    list_filter = ["categoria"]

    actions = ["tornar_discente", "tornar_docente"]

    @admin.display(description="Artigos")
    def artigos_enviados(self, obj):
        return f"{len(obj.artigos.all())}"

    @admin.display(description="Livros")
    def livros_publicados(self, obj):
        return f"{len(obj.livros.all())}"

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

    @admin.action(description="Tornar docente")
    def tornar_docente(self, request, queryset):
        updated = queryset.update(categoria="DOC")
        self.message_user(
            request,
            ngettext(
                "%d autor atualizado como docente",
                "%d autores atualizados como docentes",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )


class MesListFilter(admin.SimpleListFilter):
    title = _("mês de publicação")
    parameter_name = "mes"

    def lookups(self, request, model_admin):
        return [
            (1, _("janeiro")),
            (2, _("fevereiro")),
            (3, _("março")),
            (4, _("abril")),
            (5, _("maio")),
            (6, _("junho")),
            (7, _("julho")),
            (8, _("agosto")),
            (9, _("setembro")),
            (10, _("outubro")),
            (11, _("novembro")),
            (12, _("dezembro")),
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(
                data_aplicacao__month=self.value(),
            )


class SubmissaoAdmin(admin.ModelAdmin):
    list_display = ["artigo", "autor", "data", "aprovado"]

    list_filter = [MesListFilter]

    @admin.display(description="Data de aplicação")
    def data(self, obj):
        return obj.data_aplicacao


admin.site.register(Autor, AutorAdmin)
admin.site.register(Livro)
admin.site.register(Artigo)
admin.site.register(Submissao, SubmissaoAdmin)

admin.site.site_title = "Chuck Norris API"
admin.site.index_title = "Início"
admin.site.site_header = "Administração de Chuck Norris API"
