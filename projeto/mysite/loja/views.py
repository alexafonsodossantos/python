from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Produto, User, Cart
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

def cart(request, username):
    u = User.objects.get(username=username)
    cart = Cart.objects.filter(username = u)
    template = loader.get_template('loja/cart.html')
    context = {
        'cart': cart,
    }
    return HttpResponse(template.render(context, request))

def cart_add(request):
    if request.user.is_authenticated:
        u = User.objects.get(username= request.POST.get('username'))
        p = Produto.objects.get(id= request.POST.get('product_id'))
        if len(Cart.objects.filter(username=u, produtos_id=p ))>0:
            cart_exists = Cart.objects.get(username=u, produtos_id=p )
            p = Produto.objects.get(id= request.POST.get('product_id'))
            q = request.POST.get('qtd') 
            update_cart = Cart(pk=int(cart_exists.pk), username=u, produtos_id=p, qtd = cart_exists.qtd + int(q))
            update_cart.save()
        else:
            u = User.objects.get(username= request.POST.get('username'))
            p = Produto.objects.get(id= request.POST.get('product_id'))
            q = request.POST.get('qtd')
            cart_instance = Cart.objects.create(username=u, produtos_id = p, qtd=q)
    else:
        return redirect('/accounts/login')

    return redirect('/loja/cart/'+str(u))