from django.test import TestCase

from escola.models import Artigo, Autor, Livro, Submissao


# Create your tests here.
class LivrosTest(TestCase):
    def setUp(self):
        reperquilson = Autor.objects.create(nome="Reperquilson Bastos")
        reperqueli = Autor.objects.create(nome="Reperqueli Bastos")
        pum = Autor.objects.create(nome="Pum Godofredo Bastos")
        cumbuca = Autor.objects.create(
            nome="Maria da Cumbuca Anita Meiolina Saponilda Baratucha Al'Gat"
        )
        potinho = Autor.objects.create(nome="Vicente do Pote")

        Livro.objects.create(titulo="Dez formas de ignorar o seu humano", autor=cumbuca)
        Livro.objects.create(titulo="A arte gloriosa de destruir tudo", autor=potinho)
        Livro.objects.create(titulo="Je suis un bon garçon", autor=pum)
        Livro.objects.create(titulo="PMBOK aos 18 anos", autor=reperqueli)
        Livro.objects.create(titulo="Aprenda Python em 21 minutos", autor=reperquilson)

    def test_livro_tem_autor(self):
        autor = Autor.objects.get(nome__contains="Pum")

        livro = Livro.objects.filter(autor=autor)

        self.assertIsNotNone(livro.first())


class ArtigosTest(TestCase):
    def setUp(self):
        stephanie = Autor.objects.create(nome="Stephanie Bastos")
        felipe = Autor.objects.create(nome="Felipe Bastos")

        artigo1 = Artigo.objects.create(titulo="As cores e a felicidade")
        artigo2 = Artigo.objects.create(titulo="Pinte o sete")

        stephanie.artigos.add(artigo1)
        stephanie.artigos.add(artigo2)

        felipe.artigos.add(artigo2)

    def test_busca_many_to_many(self):
        artigo = Artigo.objects.get(titulo__contains="pinte")

        autores = artigo.autor_set.all()

        self.assertEqual(len(autores), 2)


class SubmissaoTest(TestCase):
    def setUp(self):
        self.stephanie = Autor.objects.create(nome="Stephanie Bastos")
        self.felipe = Autor.objects.create(nome="Felipe Bastos")

        self.artigo1 = Artigo.objects.create(titulo="As cores e a felicidade")
        self.artigo2 = Artigo.objects.create(titulo="Pinte o sete")
        self.artigo3 = Artigo.objects.create(titulo="Pinte o oito")

        self.stephanie.artigos.add(self.artigo1)
        self.stephanie.artigos.add(self.artigo2)
        self.stephanie.artigos.add(self.artigo3)

        self.felipe.artigos.add(self.artigo2)
        self.felipe.artigos.add(self.artigo3)

        Submissao.objects.create(autor=self.stephanie, artigo=self.artigo1)
        Submissao.objects.create(autor=self.felipe, artigo=self.artigo2)
        Submissao.objects.create(autor=self.stephanie, artigo=self.artigo3)

    def test_busca_many_to_many(self):
        artigo = Artigo.objects.get(titulo__contains="cores")

        autor = artigo.autor_submissoes.all().first()

        submissoes = Submissao.objects.filter(autor=self.stephanie)

        self.assertIsNotNone(autor)
        self.assertEqual(len(submissoes), 2)
