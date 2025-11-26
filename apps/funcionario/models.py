from django.db import models
from biblioteca.models import Biblioteca

# Após o comentario "# Create your models here." e crie a classe "Order" do modelo.

class Funcionario(models.Model):

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        ordering =['id']

    def __str__(self):
        return self.nome 
