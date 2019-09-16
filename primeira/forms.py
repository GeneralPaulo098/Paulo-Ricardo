from django.forms import ModelForm
from . models import Produto
from . models import CarrinhoDeCompras, Cliente


class ProdutoForm(ModelForm):
    class Meta():
        model = Produto
        fields = '__all__'

class CarrinhoDeComprasForm(ModelForm):
    class Meta():
        model = CarrinhoDeCompras
        fields = '__all__'
        
class Cliente(ModelForm):
    class Meta():
        model = Cliente
        fields = '__all__'