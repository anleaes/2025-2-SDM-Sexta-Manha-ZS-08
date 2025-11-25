from django.db import models

# Create your models here.
class Biblioteca(models.Model):
    nome = models.CharField('Nome completo', max_length=50)

    class Meta:
        verbose_name = 'Biblioteca'
        verbose_name_plural = 'Bibliotecas'
        ordering =['id']

    def __str__(self):
        return self.nome
