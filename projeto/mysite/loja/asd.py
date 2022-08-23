def cart_add(request):
    #check if user is authenticated
    if request.user.is_authenticated:
        u = User.objects.get(username= request.POST.get('username'))
        #if it is, checks if it already has a cart
        if len(User.objects.filter(username= request.POST.get('username')))>0:
            #if it has, get product id and qtd and save into model
            p = Produto.objects.get(id= request.POST.get('product_id'))
            q = request.POST.get('qtd')
            cart_exists = Cart.objects.get(username=u, produtos_id=p )
            update_cart = Cart(pk=int(cart_exists.pk), username=u, produtos_id=p, qtd = cart_exists.qtd + int(q))
            update_cart.save()
        else:
            cart_instance = Cart.objects.create(username=u, produtos_id = p, qtd=q)
    else:
        return redirect('/accounts/login')

    return redirect('/loja/cart/'+str(u))