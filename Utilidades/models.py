from django.db import models

class Utilidade(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(null=True)
    horario_func = models.TextField(null=True)
    idade_minima = models.IntegerField(null=True)

    def __str__(self):
        return self.nome

