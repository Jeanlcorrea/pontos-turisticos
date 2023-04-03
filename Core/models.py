from django.db import models
from Utilidades.models import Utilidade
from Comentarios.models import Comentario
from Avaliacoes.models import Avaliacao
from Enderecos.models import Endereco


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    Utilidades = models.ManyToManyField(Utilidade)
    Comentarios = models.ManyToManyField(Comentario)
    Avaliacoes = models.ManyToManyField(Avaliacao)
    Enderecos = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


