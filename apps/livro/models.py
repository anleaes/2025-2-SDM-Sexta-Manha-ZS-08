from django.db import models
#from products.models import Product
#from orders.models import Order
from autor.models import Autor
from editora.models import Editora
#from exemplar.models import Exemplar
# Create your models here.

# Após o comentario "# Create your models here." e crie a classe "Livro" do modelo.

class Livro(models.Model):

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering =['id']

    def __str__(self):
        return f"{self.title} - {self.autor} - {self.editora}"