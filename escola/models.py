from django.db import models


# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=100)
    artigos = models.ManyToManyField("Artigo")
    submissoes = models.ManyToManyField(
        "Artigo", through="Submissao", related_name="autor_submissoes"
    )


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)


class Artigo(models.Model):
    titulo = models.CharField(max_length=200)


class Submissao(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)

    data_aplicacao = models.DateField(auto_now=True)
    aprovado = models.BooleanField(default=False)
