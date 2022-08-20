from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Produto
from django.template import loader

def index(request):
    latest_produto_list = Produto.objects.order_by('id')
    template = loader.get_template('loja/index.html')
    context = {
        'latest_produto_list': latest_produto_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'loja/detail.html', {'produto': produto})

def promocoes(request):
    return render(request, 'loja/promocoes.html')

def categorias(request):
    return render(request, 'loja/categorias.html')

def perfil(request):
    return render(request, 'loja/perfil.html')