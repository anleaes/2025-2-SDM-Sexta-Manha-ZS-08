from django.db import models
from biblioteca.models import Biblioteca
from livro.models import Livro
# Create your models here.

# Após o comentario "# Create your models here." e crie a classe "Exemplar" do modelo.
class Exemplar(models.Model):

    class Meta:
        verbose_name = 'Exemplar'
        verbose_name_plural = 'Exemplares'
        ordering =['id']

    def __str__(self):
        return self.codigo_de_barras - self.livro.titulo