from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=300)
    telefone = models.CharField(max_length=30)
    data_nascimento = models.DateTimeField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome