from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Artigo(models.Model):
    
    titulo =  models.CharField('Titulo', max_length=50)
    texto = models.TextField('Corpo')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField('Criado em', auto_now_add=True)
    data_pub =  models.DateTimeField('Publicado em')
