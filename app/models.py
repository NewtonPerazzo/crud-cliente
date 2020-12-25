from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Cliente(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=300)
    telefone = models.CharField(max_length=30)
    data_nascimento = models.DateField(null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


