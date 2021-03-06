from django.db import models

class Autor(models.Model):
    nome=models.CharField(max_length=255)
    idade=models.IntegerField()

    def __str__(self):
        return '%s [%s]' %(self.nome, self.idade)

class Editora(models.Model):
    nome = models.CharField(max_length=255)
    avaliacao = models.IntegerField()

    def __str__(self):
        return '%s' %(self.nome)


class Livro(models.Model):
    nome = models.IntegerField
    preco = models.DecimalField (max_digits=10, decimal_places=2)
    avaliacao = models.FloatField()
    autores = models.FloatField()
    autores=models.ManyToManyField(Autor)
    editora=models.ForeignKey(Editora, on_delete=models.CASCADE)
    data_pub =models.DateField()

class Loja(models.Model):
    name = models.CharField(max_length=255)
    livros = models.ManyToManyField(Livro)
    quantidade_de_clientes = models.PositiveIntegerField()