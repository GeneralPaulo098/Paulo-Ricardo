from django.db import models

class CarrinhoDeCompras(models.Model):
    tamanho = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    CarrinhoDeCompras = models.OneToOneField(CarrinhoDeCompras,on_delete=models.CASCADE,primary_key=True)

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    codigo = models.IntegerField()
    carrinho = models.ForeignKey(CarrinhoDeCompras, on_delete=models.CASCADE)






