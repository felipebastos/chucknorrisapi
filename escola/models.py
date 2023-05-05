from django.db import models

CATEGORIA = (
    ("DOC", "Docente"),
    ("DIS", "Discente"),
    ("SC", "Sem categoria"),
)


# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=100)
    artigos = models.ManyToManyField("Artigo")
    submissoes = models.ManyToManyField(
        "Artigo", through="Submissao", related_name="autor_submissoes"
    )

    categoria = models.CharField(max_length=3, choices=CATEGORIA, default="SC")

    def __str__(self) -> str:
        return f"PhD. {self.nome}"

    class Meta:
        verbose_name_plural = "autores"


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="livros")


class Artigo(models.Model):
    titulo = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.titulo}"


class Submissao(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)

    data_aplicacao = models.DateField(auto_now=True)
    aprovado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.artigo} - {self.autor}"

    class Meta:
        verbose_name = "submissão"
        verbose_name_plural = "submissões"
