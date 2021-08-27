from django.db import models
from django.db.models.base import Model

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100) # campo de texto
    dt_criacao = models.DateTimeField(auto_now_add=True) # data de criacao da categoria

    def __str__(self):
        return self.nome


class Transacao(models.Model):
    data = models.DateTimeField(auto_now_add=True) # data da transacao
    data = models.DateTimeField() # data manual
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Transacoes'

    def __str__(self):
        return self.descricao