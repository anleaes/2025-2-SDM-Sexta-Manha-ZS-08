from django.db import models
from usuario.models import Usuario
from funcionario.models import Funcionario
from exemplar.models import Exemplar
# Create your models here.

# Após o comentario "# Create your models here." e crie a classe "Order" do modelo.
class Emprestimo(models.Model):
    data_emprestimo = models.DateField('Data de Empréstimo')
    data_devolucao_prevista = models.DateField('Data de Devolução Prevista')
    data_devolucao = models.DateField('Data de Devolução')
    status = models.CharField('Status', max_length=20)
    renovacoes_realizadas = models.IntegerField('Renovações Realizadas', default=0)
    max_renovacoes = models.IntegerField('Máximo de Renovações', default=2)
    
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    exemplar = models.ForeignKey(Exemplar, on_delete=models.CASCADE, null=True)

    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    # isso significa que se o usuario/funcionario for deletado, todos os emprestimos relacionados a ele serao deletados tbm
    #talvez seja interessante isso nao ocorrer para funcionarios, mas vou manter para deixar igual o diagrama

    class Meta:
        verbose_name = 'Emprestimo'
        verbose_name_plural = 'Emprestimos'
        ordering =['id']

    def __str__(self):
        return f"{self.id} - {self.usuario} - {self.exemplar} - {self.status}" 
