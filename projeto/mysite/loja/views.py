from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Produto, User, Cart
from django.template import loader
from decimal import Decimal
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse

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
        img = Produto.objects.get(id= request.POST.get('product_id')).prod_img
        v = Produto.objects.get(id= request.POST.get('product_id')).preço
        if len(Cart.objects.filter(username=u, produtos_id=p ))>0:
            cart_exists = Cart.objects.get(username=u, produtos_id=p )
            img = Produto.objects.get(id= request.POST.get('product_id')).prod_img
            p = Produto.objects.get(id= request.POST.get('product_id'))
            q = request.POST.get('qtd')
            v = Produto.objects.get(id= request.POST.get('product_id')).preço 
            update_cart = Cart(pk=int(cart_exists.pk), username=u, produtos_id=p, qtd = cart_exists.qtd + int(q), prod_img=img, preço = float(v))
            update_cart.save()
        else:
            img = Produto.objects.get(id= request.POST.get('product_id')).prod_img
            u = User.objects.get(username= request.POST.get('username'))
            p = Produto.objects.get(id= request.POST.get('product_id'))
            q = request.POST.get('qtd')
            v = Produto.objects.get(id= request.POST.get('product_id')).preço
            cart_instance = Cart.objects.create(username=u, produtos_id = p, qtd=q, prod_img = img, preço = float(v))
    else:
        return redirect('/accounts/login')
    return redirect('/loja/cart/'+str(u))


def update_cart(request):
    query_dict = request.POST
    print(query_dict)
    qtds = request.POST.getlist('number')
    product_ids = request.POST.getlist('product_id')
    produtos_id = request.POST.getlist('produto_nome')
    print(product_ids)

    u = User.objects.get(username= request.POST.get('username'))

    for a in product_ids:
        index = product_ids.index(a)
        p = Produto.objects.get(id = produtos_id[index])
        cart_exists = Cart.objects.get(username=u, produtos_id=p)
        update_cart = Cart(pk=int(cart_exists.pk), username=u, produtos_id=p, qtd = int(qtds[index]), preço = cart_exists.preço, prod_img = cart_exists.prod_img)
        update_cart.save()

    return redirect('/loja/checkout/'+str(u))


def checkout(request, username):
    u = User.objects.get(username=username)
    cart_items = Cart.objects.filter(username = u)
    total = 0
    for a in cart_items:
        subtotal = a.preço * a.qtd
        total += subtotal
    template = loader.get_template('loja/checkout.html')
    context = {
        'cart_items': cart_items,
        'total' : total,
    }
    return HttpResponse(template.render(context, request))
