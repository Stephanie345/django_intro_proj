from django.db import models

# Create your models here.

class Artigo(models.Model):
    
    titulo =  models.CharField('Titulo', max_length=50)
    texto = models.TextField('Corpo')
    autor = models.CharField('Autor', max_length=50)
    data_criacao = models.DateTimeField('Criado em', auto_now_add=True)
    data_pub =  models.DateTimeField('Publicado em')
