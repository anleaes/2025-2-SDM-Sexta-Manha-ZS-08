from django.db import models

# Create your models here.
# Após o comentario "# Create your models here." e crie a classe "Autor" do modelo.

class Autor(models.Model):
    nome = models.CharField('Nome', max_length=50)
