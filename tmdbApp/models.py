from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Comida(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    area = models.CharField(max_length=200)
    instrucoes = models.TextField()
    imagem = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome