from django.db import models
from usuario.models import Usuario
from funcionario.models import Funcionario
from exemplar.models import Exemplar

# Create your models here.

# Após o comentario "# Create your models here." e crie a classe "Order" do modelo.
class Emprestimo(models.Model):

    class Meta:
        verbose_name = 'Emprestimo'
        verbose_name_plural = 'Emprestimos'
        ordering =['id']

    def __str__(self):
        return f"{self.id} - {self.usuario} - {self.exemplar} - {self.status}" 
