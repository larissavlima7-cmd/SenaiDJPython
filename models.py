from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Tabela de categoria de receitas
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

#Tabela de receitas
class Receita(models.Model):
    #Atributos da classe receita
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.IntegerField()
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)
    foto_receita = models.ImageField(upload_to='receitas/fotos', blank=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)