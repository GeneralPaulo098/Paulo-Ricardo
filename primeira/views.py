from django.shortcuts import render,redirect
from . models import Produto
from . forms import ProdutoForm
from django.db.models.fields import Field
from django.db.models import IntegerField
from django.contrib import messages

def home(request):
    return render(request,'home.html')

def produto_list(request):
    produtos = Produto.objects.all()
    return render(request,'produto/list.html',{'produtos':produtos})


def produto_show(request,id):
    produto = Produto.objects.get(pk=id)
    return render(request, 'produto/show.html',{'produto':produto})

def produto_delete(request,id):
    Produto.objects.get(pk=id).delete()
    return redirect('/primeira/produto/')

def editar(request,id):
    if(request.method=='POST'):
        produto = Produto.objects.get(pk=id)
        form = ProdutoForm(request.POST ,instance = produto)
        if form.is_valid():
            form.save()
            return redirect('/primeira/produto/')
        else:
            return render(request,'produto/editar.html',{'form':form, 'id':id})        
    else:
        produto = Produto.objects.get(pk=id)
        form = ProdutoForm(instance = produto)
        return render(request,'produto/editar.html',{'form':form,'id':id})

def create(request):
    if(request.method=='POST'):
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'produto adicionado com sucesso!')
            return redirect('/primeira/produto/')
        else:
            return render(request,'produto/form.html',{'form':form})     
    else:
        form = ProdutoForm()
        return render(request,'produto/form.html',{'form':form})


def pesquisa(request):
    if (request.method=='POST'):
        q = request.POST.get('pesquisar')   
        produtos = Produto.objects.filter(nome__icontains=q)
        return render(request,'produto/list.html',{'produtos':produtos})