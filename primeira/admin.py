from django.contrib import admin

from . models import Produto, Cliente, CarrinhoDeCompras

admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(CarrinhoDeCompras)
