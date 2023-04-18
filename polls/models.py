from django.db import models


# Create your models here.
class Pergunta(models.Model):
    texto = models.CharField(max_length=144)

    def __str__(self) -> str:
        return str(self.texto)


class Opcao(models.Model):
    texto = models.CharField(max_length=100)

    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.texto)
