from django.shortcuts import redirect, render

from products.models import Product

from .models import Cart

def cart_home(request):
    cart, is_new= Cart.objects.get_or_new(request)
    context = {
        "cart": cart
    }
    return render(request, "carts/home.html", context)

def cart_update(request):
    # print(dir(request.POST))
    print(request.POST)
    # print(request.POST)
    # print(request.path_info)
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj= Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show Message to User: Product is unavailable")
            return redirect('carts:home')
        product_obj = Product.objects.get(id=product_id)
        cart, is_new= Cart.objects.get_or_new(request)
        if product_obj in cart.products.all():
            cart.products.remove(product_obj)
        else:
        # This is how we add a many-many relationship. Not by directly doing cart_obj.save() as we would do to change cart attributes
            cart.products.add(product_obj) # cart.products.add(product_id)
        request.session['cart_items'] = cart.products.count()
    return redirect('carts:home')