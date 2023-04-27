from django.db import models

from django.contrib.auth import get_user_model


# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=128)
    texto = models.TextField()

    autor = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.SET_NULL, related_name="postagens"
    )

    def __str__(self) -> str:
        return f"{self.titulo}"


class Comentario(models.Model):
    texto = models.TextField()

    autor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    postagem = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.texto}"
