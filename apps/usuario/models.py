from django.db import models

# Create your models here.

class Usuario(models.Model):

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering =['id']

    def __str__(self):
        return self.nome