from django.db import models

# Create your models here.
# Cria a tabela Pessoas no db
class Pessoas(models.Model):
    cpf = models.BigIntegerField()
    nome = models.CharField(max_length=60)
    profissão = models.CharField(max_length=25)

    def __str__(self):
        return self.nome
        # de vez ficar pessoa(1), vai exibir o nome

