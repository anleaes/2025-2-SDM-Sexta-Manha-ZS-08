from django.db import models

# Create your models here.
class Editora(models.Model):

    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'
        ordering =['id']

    def __str__(self):
        return self.nome