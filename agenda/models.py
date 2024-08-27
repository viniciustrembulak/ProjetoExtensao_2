from django.db import models

# Create your models here.
from django.db import models

class Agendamento(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data = models.DateTimeField()
    servico = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome} - {self.servico} em {self.data}'
