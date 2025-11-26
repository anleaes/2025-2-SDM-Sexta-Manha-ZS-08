from django.db import models
from biblioteca.models import Biblioteca
from livro.models import Livro
# Create your models here.


    class Meta:
        verbose_name = 'Exemplar'
        verbose_name_plural = 'Exemplares'
        ordering =['id']

    def __str__(self):
        return self.codigo_de_barras - self.livro.titulo